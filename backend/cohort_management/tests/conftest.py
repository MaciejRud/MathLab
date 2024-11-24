"""
Configurations for pytest.
"""

import contextlib
import pytest

from httpx import AsyncClient, ASGITransport
from typing import AsyncGenerator

from cohort_management.src.utils.database import engine, get_db
from cohort_management.src.models.model import Base
from cohort_management.src.main import app

get_async_session_context = contextlib.asynccontextmanager(get_db)


@pytest.fixture(scope='session')
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
async def db_setup():
    """Create and drop the database tables for testing."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def async_client(db_setup) -> AsyncGenerator:
    """Asynchronous HTTP client for testing."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.fixture
async def db_session(db_setup) -> AsyncGenerator:
    """Temporary in-memory database session for testing."""
    async with get_async_session_context() as session:
        yield session
