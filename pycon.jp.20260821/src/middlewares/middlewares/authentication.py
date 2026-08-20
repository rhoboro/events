# uv run unauthorized_authentication.py
# curl http://127.0.0.1:8000/auth
# curl http://127.0.0.1:8000/auth -u rhoboro:secret
#
# uv run authentication.py
# curl http://127.0.0.1:8000/auth -u rhoboro:secret
# curl http://127.0.0.1:8000/auth -u rhoboro:invalid
import base64
from collections.abc import Callable

from starlette.requests import Request
from starlette.responses import JSONResponse


type AuthBackend = Callable[[Request], str | None]

BASIC_USER = "rhoboro"
BASIC_PASS = "secret"


def basic_auth(request: Request) -> str | None:
    """簡易Basic認証(実運用には向かない)"""
    token = request.headers.get("authorization")
    if not token or not token.startswith("Basic "):
        return None

    decoded = base64.b64decode(token.removeprefix("Basic ")).decode("utf-8")
    username, password = decoded.split(":")
    if (username, password) != (BASIC_USER, BASIC_PASS):
        return None

    return username


class UnauthorizedAuthentication:
    def __init__(self, app, auth_backend: AuthBackend):
        self.app = app
        self.auth_backend = auth_backend

    async def __call__(self, scope, receive, send):
        request = Request(scope)
        username = self.auth_backend(request)
        if not username:
            response = JSONResponse({"message": "ng"}, status_code=401)
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)


class Authentication:
    def __init__(self, app, auth_backend: AuthBackend):
        self.app = app
        self.auth_backend = auth_backend

    async def __call__(self, scope, receive, send):
        request = Request(scope)
        username = self.auth_backend(request)
        if username:
            request.state.user = username
        else:
            request.state.user = None

        await self.app(scope, receive, send)
