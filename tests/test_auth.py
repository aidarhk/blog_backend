import pytest
from tests.conftest import test_client

def test_posts_list(test_client):
    response = test_client.get("/api/v1/posts")
    assert response.status_code == 200

def test_register(test_client):
    response = test_client.post("/api/v1/auth/register", json={
        "email": "test2@example.com",
        "password": "secret123",
        "is_admin": False
    })
    assert response.status_code in [200, 201] 

def test_categories_list(test_client):
    response = test_client.get("/api/v1/categories")
    assert response.status_code == 200
