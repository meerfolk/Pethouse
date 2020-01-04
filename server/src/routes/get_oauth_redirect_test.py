import pytest
import requests_mock

from assertpy import assert_that

from src.app import create_app
from src.config import get_config

@pytest.fixture
def app():
  app = create_app()
  return app

def test_oauth_redirect(client):
  code = 'test_code'

  server = get_config()['server']
  protocol = server['protocol']
  host = server['host']
  port = server['port']

  github = get_config()['github_app']
  cliendId = github['client_id']
  clientSecret = github['client_secret']

  access_token_response = {
    'access_token': 'test_access_token',
    'scope': 'test_scope',
    'token_type': 'test_token_type',
  }

  access_token_url = f'https://github.com/login/oauth/access_token?client_id={cliendId}&client_secret={clientSecret}&code={code}'

  request_url = None

  def oauth_json(req, _):
    nonlocal request_url
    request_url = req.url
    return access_token_response

  with requests_mock.Mocker() as m:
    m.post(
      access_token_url,
      json=oauth_json,
    )

    m.get('https://api.github.com/user')

    response = client.get(f'/api/oauth/redirect?code={code}')

  assert_that(request_url).is_equal_to(access_token_url)
  assert_that(response.status_code).is_equal_to(302)
  assert_that(response.location).is_equal_to(f'{protocol}://{host}:{port}/')