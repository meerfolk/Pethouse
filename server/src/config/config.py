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

def _dict_merge(dct, merge_dct):
  for k, _ in merge_dct.items():
    if (k in dct and isinstance(dct[k], dict)):
      _dict_merge(dct[k], merge_dct[k])
    else:
      dct[k] = merge_dct[k]

def _add_file_to_config(file_name):
  global config_data
  try:
    with open(get_full_path(file_name)) as json_file:
      _dict_merge(config_data, json.load(json_file))
  except IOError:
    print(f'{file_name} config not loaded')

def init():
  _add_file_to_config('default.json')
  mode = os.environ.get('MODE', 'development')
  _add_file_to_config(f'{mode}.json')
  _add_file_to_config('local.json')

  config_data['postgres']['user'] = os.environ.get('POSTGRES_USER', config_data['postgres']['user'])
  config_data['postgres']['password'] = os.environ.get('POSTGRES_PASSWORD', config_data['postgres']['password'])
  config_data['postgres']['database'] = os.environ.get('POSTGRES_DB', config_data['postgres']['database'])
  config_data['postgres']['host'] = os.environ.get('POSTGRES_HOST', config_data['postgres']['host'])
