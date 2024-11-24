'''
Set up database.
'''

import os

from fastapi import FastAPI
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from contextlib import asynccontextmanager

DATABASE_URL = os.getenv('DATABASE_URL')
DB_FORCE_ROLL_BACK = os.getenv('DB_FORCE_ROLL_BACK', False)

schema_name = 'cohort_management'
metadata_obj = MetaData(schema=schema_name)

engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.async_session = async_session_maker
    yield
    await engine.dispose()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as db:
        try:
            yield db
            if DB_FORCE_ROLL_BACK:
                await db.rollback()
            else:
                await db.commit()
        except Exception as e:
            await db.rollback()
            print(f"Error during database operation: {e}")
            raise
        finally:
            await db.close()
