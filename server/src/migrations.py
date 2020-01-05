import os

from yoyo import read_migrations, get_backend

def apply():
  user = os.environ.get('POSTGRES_USER')
  password = os.environ.get('POSTGRES_PASSWORD')
  db = os.environ.get('POSTGRES_DB')

  os.system(f'pipenv run yoyo apply -b -d postgres://{user}:{password}@postgres/{db} ./migrations')
