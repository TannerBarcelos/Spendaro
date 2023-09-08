import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Convert to config file later
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_DRIVER = 'postgresql+psycopg2'

class PGDatabaseConnector():
    SQLALCHEMY_DATABASE_URL = f"{POSTGRES_DRIVER}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"       # Postgres connection string
    engine = create_engine(SQLALCHEMY_DATABASE_URL)                                                                                 # Create a new DB Engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)                                                     # Create a db session
    Base = declarative_base()                                                                                                       # Create a base class for models

    # Yields a db session to the caller and closes the session when the caller is done (used to bind the session to the request lifecycle)
    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Connect to the database
    def connect(self):
        try:
            self.engine.connect()
            print('Connected to database')
        except Exception as e:
            print(f'Error connecting to database: {e}')
            raise e
