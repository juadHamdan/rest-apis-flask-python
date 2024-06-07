class TestItemEndpoints:

    def test_create_item(self, client):
        response = client.post("/store/2/item", json={"name": "Test Item", "price": 10.5})
        assert response.status_code == 201
        assert response.get_json() == {"name": "Test Item", "price": 10.5}

    def test_create_item_in_nonexistent_store(self, client):
        response = client.post("/store/999/item", json={"name": "Test Item", "price": 10.5})
        assert response.status_code == 404
        assert response.get_json() == {"message": "Store not found"}

    def test_get_item_in_store(self, client):
        response = client.get("/store/1/item")
        assert response.status_code == 200
        assert response.get_json() == {"items": [{"id": 1, "name": "Chair", "price": 15.99}]}

    def test_get_item_in_nonexistent_store(self, client):
        response = client.get("/store/999/item")
        assert response.status_code == 404
        assert response.get_json() == {"message": "Store not found"}

    def __repr__(self) -> str:
        return "TestItemEndpoints"