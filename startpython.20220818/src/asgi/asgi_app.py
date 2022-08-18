async def simple_app(scope, receive, send):
    assert scope["type"] == "http"
    print(f"{scope=}")
    event = await receive()
    print(f"{event=}")
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": event["body"],
        }
    )
