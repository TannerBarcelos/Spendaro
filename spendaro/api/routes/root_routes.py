from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from controllers.root_controller import RootController
from routes.route_utils import HTTPMethods

class RootRouter:
    def __init__(self, db: PGDatabaseConnector):
        
        self.router = APIRouter()
        self.controller = RootController(db)

        # Register routes from root controller (controllers are mapped to a specific router which is registered to a top level router)
        self.router.add_api_route('/', self.controller.read_root, methods=[HTTPMethods.GET.value])