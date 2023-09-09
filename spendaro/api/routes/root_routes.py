from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from controllers.root_controller import RootControllers
from .lib.http import HTTPMethods

class RootRouter:
    def __init__(self, db: PGDatabaseConnector):
        self.router = APIRouter()
        self.controllers = RootControllers(db)

        '''
        Register routes here
        '''
        # GET /api/root/dummy
        self.router.add_api_route('/', self.controllers.dummy, methods=[HTTPMethods.GET.value])
        
        # GET /api/root/dummy/{name}
        self.router.add_api_route('/{name}', self.controllers.dummyname, methods=[HTTPMethods.GET.value])