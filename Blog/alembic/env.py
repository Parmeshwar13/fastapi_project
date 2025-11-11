from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy import pool
from alembic import context

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import your Base and models
from database import Base  # make sure database.py has Base = declarative_base()
from models import *       # import your models here

# Alembic Config object
config = context.config
fileConfig(config.config_file_name)

# --- Your DB URL ---
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/blogdb"

connectable = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=pool.NullPool)

def run_migrations_online():
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=Base.metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
