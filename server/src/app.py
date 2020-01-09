from flask import Flask
from src import routes
from src.config import init as init_config
from src.config import get_config
from src.database.db import init as init_database

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

  global app
  app = Flask(__name__)

  with app.app_context():
    init_database()

  register_blueprints(app)

  return app


