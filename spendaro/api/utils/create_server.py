from fastapi import FastAPI

class FastApiServerCreator:
    def __init__(self):
        self.__app__ = FastAPI()

    def get_app(self):
        return self.__app__