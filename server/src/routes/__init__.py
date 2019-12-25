import requests
from flask import Blueprint, request
from src.config import get_config

blueprint = Blueprint('routes', __name__)

@blueprint.route('/login')
def login():
  return 'login'


@blueprint.route('/config')
def config():
  return 'config'

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

