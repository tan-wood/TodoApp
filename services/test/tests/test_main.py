from starlette.testclient import TestClient
import sys


from backend.src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == 'Hello, World!'