from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from routes.root_routes import RootRouter

router: APIRouter = APIRouter()
db: PGDatabaseConnector = PGDatabaseConnector()

# Register controllers
root_routes = RootRouter(db)

# Register routes
router.include_router(root_routes.router, prefix='/root')
