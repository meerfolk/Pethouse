import pytest
from src.app import create_app
from assertpy import assert_that
from src.config import get_config, get_url


@pytest.fixture
def app():
  app = create_app()
  return app


def test_config(client):
  response = client.get('/api/config')
  assert_that(response.status_code).is_equal_to(200)
  assert_that(response.json).is_equal_to({
    'github': {
      'client_id': get_config()['github_app']['client_id'],
      'redirect_uri': get_url(get_config()['github_app']['redirect_uri'])
    }
  })

