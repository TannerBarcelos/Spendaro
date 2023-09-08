from utils.create_server import FastApiServerCreator
from db.connect_db import PGDatabaseConnector as DatabaseConnector

server = FastApiServerCreator()
app = server.get_server()

db = DatabaseConnector()
db.connect()

@app.get("/api")
def read_root(name: str = 'world'):
    name = name.capitalize()
    return {"greeting": f"Hello {name}"}