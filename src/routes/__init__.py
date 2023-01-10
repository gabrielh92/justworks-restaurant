from src.server import server

@server.get("/")
def home():
    return "Justworks Restaurant by Gabriel Hruskovec"
