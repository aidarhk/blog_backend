import pytest
import sys
import os

sys.path.insert(0, "/app")

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    return client
