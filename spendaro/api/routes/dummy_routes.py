from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from controllers.dummy import DummyController
from .lib.http import HTTPMethods, HTTPStatusCodes

class DummyRoutes:
    def __init__(self, db: PGDatabaseConnector):
        self.router = APIRouter()
        self.__controllers = DummyController(db)
 
        '''
        Register routes here for this route collection i.e /api/dummy
        '''
        # GET /api/dummy/
        self.router.add_api_route('/', self.__controllers.GET_DUMMY, methods=[HTTPMethods.GET.value], status_code=HTTPStatusCodes.OK.value)
        
        # GET /api/dummy/{name}
        self.router.add_api_route('/{name}', self.__controllers.GET_DUMMY_NAME, methods=[HTTPMethods.GET.value], status_code=HTTPStatusCodes.OK.value)
