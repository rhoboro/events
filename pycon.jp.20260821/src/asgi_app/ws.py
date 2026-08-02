# uv run uvicorn ws:app
# fmt: off
async def app(scope, receive, send):
    assert scope["type"] == "websocket"

    # ハンドシェイク
    event = await receive()
    assert event["type"] == "websocket.connect"
    await send({"type": "websocket.accept"})

    while True:
        event = await receive()
        if event["type"] == "websocket.receive":
            await send({
                "type": "websocket.send",
                "text": event["text"],
            })

        elif event["type"] == "websocket.disconnect":
            print("disconnected")
            break
