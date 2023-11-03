from utils.create_server import FastApiServerFactory
from routes.main import router

# Instantiate a new server creator
instance = FastApiServerFactory()

# Create a FastAPI App
app = instance.get_app()

# Link up routers (all routes are prefixed via /api)
app.include_router(router, prefix='/api')