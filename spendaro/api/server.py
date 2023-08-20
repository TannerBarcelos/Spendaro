from utils.create_server import FastApiServerCreator

server = FastApiServerCreator()
app = server.get_server()

@app.get("/api")
def read_root(name: str = 'world'):
    name = name.capitalize()
    return {"greeting": f"Hello {name}"}