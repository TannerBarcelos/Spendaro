from utils.server_factory import FastApiServerFactory
from routes.router import root_router as router

# Instantiate a new server using the FastApiServerFactory class
fast_api_instance = FastApiServerFactory()

# Get the app from the instance
app = fast_api_instance.get_app()

# Include the router from routes.main
app.include_router(router, prefix='/api')

# Run the server
if __name__ == '__main__':
    fast_api_instance.run_server('server:app')
