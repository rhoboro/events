# uv run health_check.py
# curl http://127.0.0.1:8000
# curl http://127.0.0.1:8000/health
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Scope, Receive, Send


class HealthCheck:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope)
        if request.url.path == "/health":
            response = JSONResponse({"message": "ok"})
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)
