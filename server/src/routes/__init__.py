import requests
from flask import Blueprint, request
from src.config import get_config, get_url

blueprint = Blueprint('routes', __name__)

@blueprint.route('/login')
def login():
  return 'login'


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
  requests.post(
    f'https://github.com/login/oauth/access_token',
    params={
      'client_id': github['client_id'],
      'client_secret': github['client_secret'],
      'code': request.args.get('code'),
    },
  )

  return 'OK'

