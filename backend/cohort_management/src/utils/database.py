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
print(f"DATABASE_URL: {DATABASE_URL}")  # Debug statement
DB_FORCE_ROLL_BACK = os.getenv('DB_FORCE_ROLL_BACK', False)

schema_name = 'cohort_management'
metadata_obj = MetaData(schema=schema_name)

engine = create_async_engine(DATABASE_URL)
print("Engine created")  # Debug statement

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
    print("Engine disposed")  # Debug statement

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as db:
        try:
            yield db
            if DB_FORCE_ROLL_BACK:
                await db.rollback()
                print("Rolling back transaction")  # Debug statement
            else:
                await db.commit()
                print("Committing transaction")  # Debug statement
        except Exception as e:
            await db.rollback()
            print(f"Error during database operation: {e}")
            raise
        finally:
            await db.close()
            print("Session closed")  # Debug statement
