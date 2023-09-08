from utils.create_server import FastApiServerCreator
from db.connect_db import PGDatabaseConnector

server = FastApiServerCreator()
app = server.get_app()

db = PGDatabaseConnector()

@app.get("/api")
def read_root(name: str = 'world'):
    return {"greeting": f"Hello {name}"}