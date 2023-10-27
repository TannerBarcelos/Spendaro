from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from controllers.root_controller import RootControllers
from .lib.http import HTTPMethods, HTTPStatusCodes

# This class is responsible for registering the routes for the root path
# and is for demonstration purposes only (can be deleted later but should follow the same structure)
class RootRoutes:
    def __init__(self, db: PGDatabaseConnector):
        self.router = APIRouter()
        self.__controllers__ = RootControllers(db)

        '''
        Register routes here
        '''
        # GET /api/root/dummy
        self.router.add_api_route('/', self.__controllers__.dummy, methods=[HTTPMethods.GET.value], status_code=HTTPStatusCodes.OK.value)
        
        # GET /api/root/dummy/{name}
        self.router.add_api_route('/{name}', self.__controllers__.dummyname, methods=[HTTPMethods.GET.value], status_code=HTTPStatusCodes.OK.value)
