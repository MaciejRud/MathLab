'''
Set up database.
'''

from fastapi import FastAPI

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from contextlib import asynccontextmanager
from .config import config

schema_name = 'cohort_management'
metadata_obj = MetaData(schema=schema_name)

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
    app.state.async_session = async_session_maker
    yield
    await engine.dispose()

