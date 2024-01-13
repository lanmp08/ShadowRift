import jwt

SECRET_KEY = "your-secret-key"

# ...

class GameServer:
    # ...

    async def handle_connection(self, websocket, path):
        try:
            # Verificar se o token JWT é válido
            token = await websocket.recv()
            try:
                jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            except jwt.InvalidTokenError:
                return

            self.connections.add(websocket)
            await self.serve_player(websocket)
        finally:
            self.connections.remove(websocket)

    # ...