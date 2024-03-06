from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Summarization Model Home"}

def test_summarize_success():
    text = "This is a test text for summarization."
    response = client.post("/summarize", json={"text": text})
    print(response.json())
    assert response.status_code == 200
    assert "summary" in response.json()
