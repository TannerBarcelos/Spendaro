from utils.create_server import FastApiServerCreator
from routes.main import router

app = FastApiServerCreator().get_app()

app.include_router(router, prefix='/api')
