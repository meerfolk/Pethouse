from flask import Flask
from src import routes

def register_blueprints(app):
  app.register_blueprint(routes.blueprint, url_prefix='/api')

def create_app():
  app = Flask(__name__)
  register_blueprints(app)
  return app


