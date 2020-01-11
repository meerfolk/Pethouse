"""
Create sessions
"""

from yoyo import step

__depends__ = {'20200104_01_A9YLQ-create-users'}

step(
  """
    CREATE TABLE "sessions" (
      session_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
      created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
      updated_at TIMESTAMPTZ,
      user_id UUID NOT NULL REFERENCES "users",
      expired_at TIMESTAMPTZ NOT NULL
    );
  """,
  'DROP TABLE "sessions";'
)
