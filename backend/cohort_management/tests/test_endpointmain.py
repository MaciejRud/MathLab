import pytest

@pytest.mark.anyio
async def test_root_endpoint(async_client):
    """Test to check if the root endpoint is reachable."""
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}  # Zakładając, że endpoint zwraca taki JSON
