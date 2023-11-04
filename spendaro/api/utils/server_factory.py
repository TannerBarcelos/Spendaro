from fastapi import FastAPI
from config import *

class FastApiServerFactory:
    def __init__(self):
        self.__app__ = FastAPI(debug=DEBUG)

    def get_app(self):
        return self.__app__