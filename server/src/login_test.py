import pytest

from src.app import create_app

@pytest.fixture
def app():
  app = create_app()
  return app

def test_login(client):
  response = client.get('/api/login')
  assert response.status_code == 200
