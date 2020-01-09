from ..db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String

class User(db.Model):
  user_id = Column(UUID, primary_key=True)
  github_login = Column(String(50), nullable=False, unique=True)
  name = Column(String(255), nullable=False)
  email = Column(String(100), nullable=False, unique=True)
  avatar_url = Column(String(100), nullable=False)

