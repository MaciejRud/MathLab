import pytest

@pytest.mark.anyio
async def test_create_item(async_client):
    """Test to check if the /items/ endpoint is reachable."""
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Test print")
    response = await async_client.post("/items/", json={"name": "item1", "description": "test item"})
    assert response.status_code == 200
    assert response.json() == {"name": "item1", "description": "test item"}
