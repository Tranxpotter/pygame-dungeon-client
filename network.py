import websockets

class Network:
    def __init__(self, uri:str) -> None:
        self.uri = uri
    
    async def connect(self):
        self.conn = await websockets.connect(self.uri)

    async def send(self, data):
        await self.conn.send(data)
    
    async def recv(self):
        return await self.conn.recv()