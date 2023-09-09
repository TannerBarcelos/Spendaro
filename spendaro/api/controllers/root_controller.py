from db.connect_db import PGDatabaseConnector
from services.mock_service import MockService

'''
Defines the controller methods for the root routes (e.g. /api/root/dummy, /api/root/dummy/{name}, etc.)
These methods are called by the router methods in routes/{some_router}.py
'''
class RootControllers:

    def __init__(self, db: PGDatabaseConnector):
        self.mock_service = MockService(db)

    # GET /api/root/dummy
    def dummy(self, name: str = 'world'):
        result = self.mock_service.sample_service_method()
        return {"greeting": f"Hello {name}. The result of 1+1 is {result}"}