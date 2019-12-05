from flask import Flask
from src import routes
from src.config import init as init_config


def register_blueprints(app):
  app.register_blueprint(routes.blueprint, url_prefix='/api')

def create_app():
  init_config()

  app = Flask(__name__)
  register_blueprints(app)

  return app


