from sqlalchemy.sql import text
from sqlalchemy import TextClause
from db.connect_db import PGDatabaseConnector

class MockService:
    def __init__(self, db: PGDatabaseConnector):
        self.db = db

    def sample_service_method(self):
        connection = self.db.get_connection()
        query: TextClause = text('SELECT 1+1')
        result = connection.execute(query).first()[0]
        connection.close()
        return result