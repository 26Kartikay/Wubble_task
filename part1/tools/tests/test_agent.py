from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_basic_prompt():
    response = client.post("/ask", json={"prompt": "What is Artificial Intelligence?"})
    assert response.status_code == 200
    assert "intelligence" in response.json()["response"].lower()

def test_empty_prompt():
    response = client.post("/ask", json={"prompt": ""})
    assert response.status_code == 200
    assert isinstance(response.json()["response"], str)

def test_search_prompt():
    response = client.post("/ask", json={"prompt": "Search for the current Prime Minister of India"})
    assert response.status_code == 200
    assert "india" in response.json()["response"].lower()

def test_funny_prompt():
    response = client.post("/ask", json={"prompt": "Tell me a joke about Python"})
    assert response.status_code == 200
    assert isinstance(response.json()["response"], str)

def test_invalid_payload():
    response = client.post("/ask", json={})
    assert response.status_code == 422  # Unprocessable Entity due to missing 'prompt'
