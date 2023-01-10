from src.server import server

@server.post("/reservations")
async def create_reservation():
    return ""
