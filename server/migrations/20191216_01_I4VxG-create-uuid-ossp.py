"""
Create uuid-ossp
"""

from yoyo import step

step(
  'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";',
  'DROP EXTENSION IF EXISTS "uuid-ossp";',
)
