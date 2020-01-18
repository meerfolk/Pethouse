from functools import wraps
from flask import g, abort, request
from datetime import datetime

from src.database.models import get_model

def decorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    session_id = request.cookies.get('session_id', None)

    if session_id == None:
      return abort(401)

    Session = get_model('Session')
    try:
      session = Session.query.filter(
        Session.session_id == session_id,
        Session.expired_at > datetime.now(),
      ).first()
    except:
      return abort(401)

    if session == None:
      return abort(401)

    g.user = session.user

    return func(*args, **kwargs)
  return wrapper

