import os

db = None

def get():
  return db

def init():
  from flask import current_app
  from flask_sqlalchemy import SQLAlchemy
  from src.config import get_config

  postgres = get_config()['postgres']
  postgres_user = postgres['user']
  postgres_password = postgres['password']
  postgres_db = postgres['database']
  postgres_host = postgres['host']

  os.system(f'pipenv run yoyo apply -b -d postgres://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db} ./migrations')

  current_app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}'
  current_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  global db
  db = SQLAlchemy(current_app) 