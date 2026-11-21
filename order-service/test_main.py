
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_order():
    order_data = {
        "customer_id": "customer001",
        "product_name": "Laptop",
        "quantity": 2,
        "price": 500.0
    }

    response = client.post("/orders", json=order_data)

    assert response.status_code == 200
    assert response.json()["product_name"] == "Laptop"
    assert response.json()["total"] == 1000.0
    assert response.json()["status"] == "created"


def test_get_orders():
    response = client.get("/orders")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_invalid_order():
    order_data = {
        "customer_id": "customer001",
        "product_name": "Laptop",
        "quantity": 0,
        "price": 500.0
    }

    response = client.post("/orders", json=order_data)

    assert response.status_code == 400
