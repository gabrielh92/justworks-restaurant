from src.server import server

@server.get("/reservations")
async def list_reservations():
    return ""
