import requests

from operator import itemgetter
from flask import Blueprint, request, redirect, g

from src.config import get_config, get_url
from src.database.models import get_model
from src.database import get_database

from .middlewares import get_user_from_session

blueprint = Blueprint('routes', __name__)

@blueprint.route('/login')
@get_user_from_session
def login():
  return {
    'name': g.user.name,
    'avatar_url': g.user.avatar_url,
  }


@blueprint.route('/config')
def config():
  github_data = get_config()['github_app']

  return {
    'github': {
      'client_id': github_data['client_id'],
      'redirect_uri': get_url(github_data['redirect_uri']),
    },
  }

@blueprint.route('/oauth/redirect')
def oauthRedirect():
  github = get_config()['github_app']
  access_token_response = requests.post(
    f'https://github.com/login/oauth/access_token',
    params={
      'client_id': github['client_id'],
      'client_secret': github['client_secret'],
      'code': request.args.get('code'),
    },
    headers={
      'Accept': 'application/json',
    },
  )

  access_token = access_token_response.json()['access_token']

  user_response = requests.get(
    'https://api.github.com/user',
    headers={
      'Authorization': f'Bearer {access_token}',
      'Accept': 'application/json',
    },
  )

  email, github_login, name, avatar_url = itemgetter('email', 'github_login', 'name', 'avatar_url')(user_response.json())
  user = get_model('User')(email=email, github_login=github_login, name=name, avatar_url=avatar_url)
  db = get_database()
  db.session.add(user)
  db.session.commit()

  return redirect(get_url(''))
