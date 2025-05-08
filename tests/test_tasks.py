from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={
        "id": 1,
        "title": "Test tarea",
        "description": "Descripción de prueba",
        "completed": False
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test tarea"

def test_get_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
