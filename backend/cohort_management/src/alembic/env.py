import asyncio
import os

from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from src.models.model import Base

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config_alembic = context.config

#Load database URL from your custom config
DATABASE_URL = os.getenv('DATABASE_URL')
config_alembic.set_main_option('sqlalchemy.url', DATABASE_URL)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config_alembic.config_file_name is not None:
    fileConfig(config_alembic.config_file_name)


target_metadata = Base.metadata
schema = target_metadata.schema



def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


def include_name(name, type_, parent_names):
    if type_ == "schema":
        return name in [schema]
    else:
        return True

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        version_table_schema="cohort_management",
        include_schemas=True,
        include_name=include_name,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    "Create an Engine and associate async connection with the context."

    connectable: AsyncEngine = create_async_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

async def run_migrations_online() -> None:
    "Run migrations in 'online' mode."

    connectable = config_alembic.attributes.get('connection', None)

    if connectable is None:
        await run_async_migrations()
    else:
        do_run_migrations(connectable)

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
