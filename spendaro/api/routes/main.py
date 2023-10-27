from fastapi import APIRouter
from db.connect_db import PGDatabaseConnector
from routes.root_routes import RootRoutes
from .lib.prefixes import RoutePrefixes as RP

router: APIRouter = APIRouter()
db: PGDatabaseConnector = PGDatabaseConnector()

# Register routes here
router.include_router(RootRoutes(db).router, prefix=RP.root.value)
# router.include_router(OtherRoutes(db).router, prefix=RP.other.value)
# router.include_router(AnotherRoutes(db).router, prefix=RP.another.value)
# router.include_router(AndAnotherRoutes(db).router, prefix=RP.and_another.value)
# router.include_router(AndSoOnRoutes(db).router, prefix=RP.and_so_on.value)