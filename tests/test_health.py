from http.client import OK


def test_health_endpoint_returns_correct_message(client):
    response = client.get("/health")

    assert response.status_code == OK
    assert response.json == {"status": "healthy"}
