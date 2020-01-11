import pytest
import requests_mock

from assertpy import assert_that

from src.app import create_app
from src.config import get_config
from src.database.models import get_model
from src.database import get_database

@pytest.yield_fixture
def app():
  app = create_app()
  yield app
  with app.app_context():
    db = get_database()
    db.session.query(get_model('User')).delete()
    db.session.commit()

def test_oauth_redirect(client):
  code = 'test_code'
  access_token = 'test_access_token'

  server = get_config()['server']
  protocol = server['protocol']
  host = server['host']
  port = server['port']

  github = get_config()['github_app']
  cliendId = github['client_id']
  clientSecret = github['client_secret']

  access_token_response = {
    'access_token': access_token,
    'scope': 'test_scope',
    'token_type': 'test_token_type',
  }

  access_token_url = f'https://github.com/login/oauth/access_token?client_id={cliendId}&client_secret={clientSecret}&code={code}'

  oauth_request_url = None
  user_headers = None

  def oauth_json(req, _):
    nonlocal oauth_request_url
    oauth_request_url = req.url
    return access_token_response

  user_response = {
    'github_login': 'test_github_login',
    'name': 'test_name',
    'email': 'test@email.com',
    'avatar_url': 'test_avatar_url',
  } 

  def user_json(req, _):
    nonlocal user_headers
    user_headers = req.headers
    return user_response

  with requests_mock.Mocker() as m:
    m.post(
      access_token_url,
      json=oauth_json,
    )

    m.get('https://api.github.com/user', json=user_json)

    response = client.get(f'/api/oauth/redirect?code={code}')

  User = get_model('User')
  user = User.query.filter_by(email=user_response['email']).first()

  assert_that(user.email).is_equal_to(user_response['email'])
  assert_that(user.name).is_equal_to(user_response['name'])
  assert_that(user.github_login).is_equal_to(user_response['github_login'])
  assert_that(user.avatar_url).is_equal_to(user_response['avatar_url'])
  assert_that(oauth_request_url).is_equal_to(access_token_url)
  assert_that(response.status_code).is_equal_to(302)
  assert_that(response.location).is_equal_to(f'{protocol}://{host}:{port}/')
  assert_that(user_headers['Authorization']).is_equal_to(f'Bearer {access_token}')