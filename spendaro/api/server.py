from utils.create_server import FastApiServerCreator as Server

server = Server()
app = server.init()

@app.get("/api")
def read_root(name: str = 'world'):
    name = name.capitalize()
    return {"greeting": f"Hello {name}"}