import pytest

from assertpy import assert_that
from datetime import datetime, timedelta

from src.app import create_app
from src.database import get_database
from src.database.models import get_model

session_id = None
expired_session_id = None

user_data = {
  'email': 'test@example.com',
  'github_login': 'test_github_login',
  'avatar_url': 'test_avatar_url',
  'name': 'test_name',
}

@pytest.yield_fixture
def app():
  app = create_app()

  with app.app_context():
    db = get_database()

    user = get_model('User')(
      email = user_data['email'],
      github_login = user_data['github_login'],
      avatar_url = user_data['avatar_url'],
      name = user_data['name'],
    )
    db.session.add(user)
    db.session.commit()

    session = get_model('Session')(
      user_id = user.user_id,
      expired_at = datetime.now() + timedelta(days=30)
    )

    expired_session = get_model('Session')(
      user_id = user.user_id,
      expired_at = datetime.now() - timedelta(days=30)
    )

    db.session.add(expired_session)
    db.session.add(session)
    db.session.commit()

    global session_id
    global expired_session_id
    session_id = session.session_id
    expired_session_id = expired_session.session_id

  yield app

  with app.app_context():
    db = get_database()
    db.session.query(get_model('Session')).delete()
    db.session.query(get_model('User')).delete()
    db.session.commit()


def test_login(client):
  client.set_cookie('/', 'session_id', session_id)
  response = client.get('/api/login')

  assert_that(response.status_code).is_equal_to(200)
  assert_that(response.json['name']).is_equal_to(user_data['name'])
  assert_that(response.json['avatar_url']).is_equal_to(user_data['avatar_url'])

def test_login_without_session(client):
  response = client.get('/api/login')

  assert_that(response.status_code).is_equal_to(401)

def test_login_session_not_found(client):
  client.set_cookie('/', 'session_id', 'test')
  response = client.get('/api/login')

  assert_that(response.status_code).is_equal_to(401)

def test_login_session_expired(client):
  client.set_cookie('/', 'session_id', expired_session_id)
  response = client.get('/api/login')

  assert_that(response.status_code).is_equal_to(401)
