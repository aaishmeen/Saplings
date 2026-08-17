from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from backend.app.connection_manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()


@app.get("/")
async def root():
    return {"message": "Saplings is alive"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            print("RECEIVED:", message)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("DISCONNECTED")