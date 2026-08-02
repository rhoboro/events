# uv run uvicorn asgi_middleware:app
# curl http://127.0.0.1:8000
from asgi_app import AsgiApp


class AsgiMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        print("Start")
        await self.app(scope, receive, send)
        print("End")


app = AsgiMiddleware(AsgiApp())
