'''
Set up database.
'''

from fastapi import FastAPI

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from contextlib import asynccontextmanager
from MathLab.core.config import config
from MathLab.models.model import Base


engine = create_async_engine(
    config.DATABASE_URL, echo=True
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()
