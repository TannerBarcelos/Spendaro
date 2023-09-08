from fastapi import FastAPI
from db.connect_db import PGDatabaseConnector

class FastApiServerCreator:
    def __init__(self):
        self.__app__ = FastAPI()                # Initialize FastAPI server
        self.__db__ = PGDatabaseConnector()     # Initialize database connector

    def init(self):
        print("Creating server...")
        print("Creating database connection...")
        self.__db__.connect()
        return self.__app__
