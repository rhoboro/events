# uv run uvicorn asgi_app:app
# curl http://127.0.0.1:8000
# fmt: off
class AsgiApp:
    async def __call__(self, scope, receive, send):
        assert scope["type"] == "http"
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [(b"content-type", b"application/json")],
        })
        await send({
            "type": "http.response.body",
            "body": b'{"message": "ok"}',
        })

app = AsgiApp()
