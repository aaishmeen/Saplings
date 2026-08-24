from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json , uuid
from backend.app.connection_manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()


@app.websocket("/ws/{room_id}/{username}")
async def websocket_endpoint(
    websocket: WebSocket,
    room_id: str,
    username: str
):
    await manager.connect(room_id, username, websocket)

    try:
        while True:
            message = await websocket.receive_text()

            try:
                data = json.loads(message)

                chat_message = {
                    "type": data["type"],
                    "id": str(uuid.uuid4()),
                    "sender": username,
                    "content": data["content"]
                }

                await manager.broadcast(room_id, json.dumps(chat_message))

            except (json.JSONDecodeError, KeyError):
                await websocket.send_text(
                    json.dumps({
                        "type": "error",
                        "message": "Invalid message format"
                    })
                )

    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)