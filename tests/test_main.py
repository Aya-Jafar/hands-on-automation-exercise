from app.main import app
from fastapi.testclient import TestClient
def test_hello():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == b"Hello, Automation!"
