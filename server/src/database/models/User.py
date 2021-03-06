from ..db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, text

class User(db.Model):
  __tablename__ = 'users'
  user_id = Column(
    UUID,
    primary_key=True,
    server_default=text('uuid_generate_v4()')
  )
  github_login = Column(String(50), nullable=False, unique=True)
  name = Column(String(255), nullable=False)
  email = Column(String(100), nullable=False, unique=True)
  avatar_url = Column(String(100), nullable=False)
