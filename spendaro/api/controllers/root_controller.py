from db.connect_db import PGDatabaseConnector
from services.mock_service import MockService

class RootController:

    def __init__(self, db: PGDatabaseConnector):
        self.mock_service = MockService(db)

    def read_root(self, name: str = 'world'):
        result = self.mock_service.sample_service_method()
        return {"greeting": f"Hello {name}. The result of 1+1 is {result}"}