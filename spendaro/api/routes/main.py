from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from routes.root_routes import RootRoutes
from .lib.prefixes import RoutePrefixes as RP

# Top level router which will be injected with other routers for each route path i.e /user, /budgets etc
root_router: APIRouter = APIRouter()

# Db Connection singleton shared across all route classes, which goes into controllers and down into services
db: PGDatabaseConnector = PGDatabaseConnector()

# Instantiate each route collection instance so we can get its router and hook it into the root apps router
root_routes = RootRoutes(db)

# Register routes here
root_router.include_router(root_routes.router, prefix=RP.root.value)