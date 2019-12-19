from flask import Blueprint

blueprint = Blueprint('routes', __name__)

@blueprint.route('/login')
def login():
  return 'login'


@blueprint.route('/config')
def config():
  return 'config'
