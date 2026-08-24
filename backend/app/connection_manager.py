from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.rooms = {}

    async def connect(self, room_id: str, username: str, websocket: WebSocket):
        await websocket.accept()

        if room_id not in self.rooms:
            self.rooms[room_id] = []

        self.rooms[room_id].append({
            "username": username,
            "websocket": websocket
        })

    def disconnect(self, room_id: str, websocket: WebSocket):
        self.rooms[room_id] = [
            connection
            for connection in self.rooms[room_id]
            if connection["websocket"] != websocket
        ]

        if not self.rooms[room_id]:
            del self.rooms[room_id]

    async def broadcast(self, room_id: str, message: str):
        for connection in self.rooms[room_id]:
            await connection["websocket"].send_text(message)