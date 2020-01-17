models = None

def init_models():
  from .Session import Session
  from .User import User

  global models
  models = {
    'User': User,
    'Session': Session,
  }

def get_model(model_name):
  return models[model_name]
