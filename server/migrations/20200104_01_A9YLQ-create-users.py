"""
Create users
"""

from yoyo import step

__depends__ = {'20191216_01_I4VxG-create-uuid-ossp'}

step(
  """
    CREATE TABLE "users" (
      user_id UUID PRIMARY KEY,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
      updated_at TIMESTAMPTZ,
      github_login VARCHAR(50) NOT NULL UNIQUE,
      name VARCHAR(255) NOT NULL,
      email VARCHAR(100) NOT NULL UNIQUE,
      avatar_url VARCHAR(100) NOT NULL
    );
  """,
  'DROP TABLE "users";',
)
