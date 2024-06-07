from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "id": 1,
        "name": "My Store",
        "items": [
            {
                "id": 1,
                "name": "Chair",
                "price": 15.99
            }
        ]
    },
    {
        "id": 2,
        "name": "Second Store",
        "items": [
            {
                "id": 1,
                "name": "Table",
                "price": 99.99
            },
            {
                "id": 2,
                "name": "Lamp",
                "price": 29.99
            }
        ]
    },
    {
        "id": 3,
        "name": "Third Store",
        "items": [
            {
                "id": 1,
                "name": "Couch",
                "price": 299.99
            },
            {
                "id": 2,
                "name": "TV",
                "price": 499.99
            }
        ]
    },
    {
        "id": 4,
        "name": "Fourth Store",
        "items": [
            {
                "id": 1,
                "name": "Couch",
                "price": 299.99
            },
            {
                "id": 2,
                "name": "TV",
                "price": 499.99
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"id": 5, "name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<int:id>/item")
def create_item(id):
    request_data = request.get_json()
    for store in stores:
        try:
            if store["id"] == id:
                new_item = {"name": request_data["name"], "price": request_data["price"]}
                store["items"].append(new_item)
                return new_item, 201
        except KeyError:
            return {"message": "Store not found"}, 404
    return {"message": "Store not found"}, 404


@app.get("/store/<int:id>")
def get_store(id):
    for store in stores:
        try:
            if store["id"] == id:
                return store
        except KeyError:
            return {"message": "Store not found"}, 404

    return {"message": "Store not found"}, 404


@app.get("/store/<int:id>/item")
def get_item_in_store(id):
    for store in stores:
        try:
            if store["id"] == id:
                return {"items": store["items"]}
        except KeyError:
            return {"message": "Store not found"}, 404
    return {"message": "Store not found"}, 404