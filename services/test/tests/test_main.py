from starlette.testclient import TestClient
import sys
from backend.src.main import app

sys.path.insert(0, '/Users/tannerwoodrum/Documents/Life/CodingProjects/TodoApp/services/backend')


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {}