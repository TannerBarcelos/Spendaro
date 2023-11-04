from db.connect_db import PGDatabaseConnector
from services.mock_service import MockService

class DummyController:

    def __init__(self, db: PGDatabaseConnector):
        self.mock_service = MockService(db)

    '''
    ---Controller method---
    http_method=GET 
    endpoint=/api/dummy/
    expected_response_code=200
    description=Returns a dummy response
    '''
    def GET_DUMMY(self):
        result = self.mock_service.sample_service_method()
        return {"greeting": f"Hello there. The result of 1+1 is {result}"}
    
    '''
    Controller method
    http_method=GET
    endpoint=/api/dummy/{name}
    expected_response_code=200
    description=Returns a dummy response with a name
    '''
    def GET_DUMMY_NAME(self, name: str = 'world'):
        result = self.mock_service.sample_service_method()
        return {"greeting": f"Hello {name}. The result of 1+1 is {result}"}