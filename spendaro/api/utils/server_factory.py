from fastapi import FastAPI
from config import DEBUG, API_DOCS_URL

class FastApiServerFactory:
    def __init__(self):
        self.__app__ = FastAPI(debug=DEBUG, docs_url=API_DOCS_URL)

    def get_app(self):
        return self.__app__