from flask import Flask
from src import routes
from src.config import init as init_config
from src.migrations import apply as apply_migrations

import os

app = None

def register_blueprints(app):
  app.register_blueprint(routes.blueprint, url_prefix='/api')

def get_app():
  if (app != None):
    return app
  else:
    return create_app()

def create_app():
  init_config()
  apply_migrations()

  global app
  app = Flask(__name__)

  register_blueprints(app)

  return app


