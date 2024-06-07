class TestStoreEndpoints:
    expected_store = {
        "id": 1,
        "name": "My Store", 
        "items": [{"id": 1, "name": "Chair", "price": 15.99}]
    }

    def test_get_stores(self, client):
        response = client.get("/store")
        assert response.status_code == 200
        data = response.get_json()

        # Check if at least one store has the expected name and items
        assert any(
            store["name"] == self.expected_store["name"] 
            and
            all(
                item in store["items"]
                for item in self.expected_store["items"]
            )
            for store in data["stores"]
        )

    def test_get_store(self, client):
        response = client.get("/store/1")
        assert response.status_code == 200
        assert response.get_json() == self.expected_store

    def test_create_store(self, client):
        response = client.post("/store", json={"name": "Test Store"})
        assert response.status_code == 201
        assert response.get_json() == {"id": 5, "name": "Test Store", "items": []}

    def test_get_nonexistent_store(self, client):
        response = client.get("/store/999")
        assert response.status_code == 404
        assert response.get_json() == {"message": "Store not found"}

    def __repr__(self) -> str:
        return "TestStoreEndpoints"
