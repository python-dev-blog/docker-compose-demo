import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


def test_health(client):
    response = client.get("/api/health")
    assert response.json() == {"status": "ok"}
