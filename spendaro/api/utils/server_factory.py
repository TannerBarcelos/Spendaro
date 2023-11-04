import uvicorn
from fastapi import FastAPI
from config import DEBUG, API_DOCS_URL, API_PORT

class FastApiServerFactory:
    def __init__(self):
        self.__app__ = FastAPI(debug=DEBUG, docs_url=API_DOCS_URL)

    def get_app(self):
        return self.__app__
    
    def run_server(self, appStr: str):
        uvicorn.run(appStr, host='0.0.0.0', port=API_PORT, reload=DEBUG)
