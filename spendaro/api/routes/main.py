from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from routes.root_routes import RootRouter
from .lib.prefixes import Prefixes

router: APIRouter = APIRouter()
db: PGDatabaseConnector = PGDatabaseConnector()

# Initialize routers
root_router = RootRouter(db)

# Register the routes
router.include_router(root_router.router, prefix=Prefixes.root.value)
