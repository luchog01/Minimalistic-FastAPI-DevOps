# test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_match():
    response = client.post(
        "/matches",
        json={"name": "Test Match", "team1": "Team A", "team2": "Team B", "result": 1},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Match"
    assert "id" in data


def test_get_matches():
    response = client.get("/matches")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_match():
    # First, create a match
    create_response = client.post(
        "/matches",
        json={"name": "Test Match", "team1": "Team A", "team2": "Team B", "result": 1},
    )
    match_id = create_response.json()["id"]

    # Then, get the match
    response = client.get(f"/matches/{match_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == match_id
    assert data["name"] == "Test Match"
