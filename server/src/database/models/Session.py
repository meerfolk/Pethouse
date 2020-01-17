from ..db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, text

class Session(db.Model):
  __tablename__ = 'sessions'
  session_id = Column(
    UUID,
    primary_key=True,
    server_default=text('uuid_generate_v4()')
  )
  user_id = Column(UUID, db.ForeignKey('users.user_id'), nullable=False)
  user = db.relationship('User', lazy='joined', uselist=False)
  expired_at = Column(DateTime, nullable=False)
