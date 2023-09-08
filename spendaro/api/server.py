from utils.create_server import FastApiServerCreator as Server
from sqlalchemy.orm import Session
from fastapi import Depends
from db.connect_db import PGDatabaseConnector as DBConnector

app = Server().get_app()
database = DBConnector().get_db()

@app.get("/api")
def read_root(name: str = 'world'):
    return {"greeting": f"Hello {name}"}