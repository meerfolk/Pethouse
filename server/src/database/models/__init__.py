def get_model(model_name):
  if model_name == 'User':
    from .User import User
    return User