import json
import os

config_data = {}

def get_full_path(path):
  return os.path.join(os.getcwd(), f'src/config/{path}')

def get_url(additional):
    protocol = config_data['server']['protocol']
    host = config_data['server']['host']
    port = config_data['server']['port']
    return f'{protocol}://{host}:{port}/{additional}'

def get_config():
  return config_data

def init():
  with open(
    get_full_path('production.json')
      if os.environ.get('MODE', 'development') == 'production' 
      else get_full_path('development.json')
    ) as json_file:
    global config_data
    config_data = json.load(json_file)