import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Convert to config file later
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

class PGDatabaseConnector():
    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"       # Postgres connection string
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})                                      # Create a new DB Engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)                                                     # Create a db session
    Base = declarative_base()                                                                                                       # Create a base class for models

    # Create a new db session
    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()