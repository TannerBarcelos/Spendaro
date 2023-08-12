from fastapi import FastAPI

class FastApiServerCreator:
    def __init__(self):
        self.__app__ = FastAPI()

    def get_server(self):
        return self.__app__
