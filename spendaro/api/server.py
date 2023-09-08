from utils.create_server import FastApiServerCreator
from db.database import PGDatabaseConnector

server = FastApiServerCreator()
app = server.get_server()

db = PGDatabaseConnector()

@app.get("/api")
def read_root(name: str = 'world'):
    name = name.capitalize()
    return {"greeting": f"Hello {name}"}