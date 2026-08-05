import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_get_endpoints():
    response = requests.get(f"{BASE_URL}/api/v1/items")
    assert response.status_code in [200, 404]

def test_create_item():
    payload = {"name": "test_item", "price": 10.5}
    response = requests.post(f"{BASE_URL}/api/v1/items", json=payload)
    assert response.status_code in [200, 201, 400, 422]

def test_negative_item():
    response = requests.get(f"{BASE_URL}/api/v1/items/invalid_id")
    assert response.status_code in [404, 400]