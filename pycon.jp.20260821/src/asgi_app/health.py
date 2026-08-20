async def app(scope, receive, send):
    assert scope["type"] == "http"

    if (scope["method"], scope["path"]) == ("GET", "/health"):
        # 固定値のヘルスチエックレスポンスを返す
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [(b"content-type", b"application/json")],
        })
        await send({
            "type": "http.response.body",
            "body": b'{"message": "ok"}',
        })

    else:
        # リクエストボディを取得し、同じ内容のエコーレスポンスを返す
        event = await receive()
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [(b"content-type", content_type(scope))],
        })
        await send({
            "type": "http.response.body",
            "body": event["body"],
        })

def content_type(scope) -> bytes:
    for name, value in scope["headers"]:
        if name == b"content-type":
            return value
    return b"text/plain"
