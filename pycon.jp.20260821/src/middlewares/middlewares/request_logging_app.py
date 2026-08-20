# uv run request_logging_app.py
# curl http://127.0.0.1:8000/request/logging -H 'content-type: application/json' -d '{"hello": "pyconjp"}'
# curl http://127.0.0.1:8000/request/logging/eager -H 'content-type: application/json' -d '{"hello": "pyconjp"}'
import json
from starlette.requests import Request
from starlette.datastructures import MutableHeaders
from .utils import is_json_content_type


class RequestLoggingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = Request(scope)
        is_request_json = is_json_content_type(request.headers.get("content-type"))

        app = LoggingApp(self.app, is_request_json)
        await app(scope, receive, send)


class LoggingApp:
    def __init__(self, app, is_request_json):
        self.app = app
        self.is_request_json = is_request_json
        self.request_body = b""
        self.is_response_json = False
        self.response_body = b""

    async def __call__(self, scope, receive, send):
        self.scope = scope
        self.receive = receive
        self.send = send

        await self.app(scope, self.my_receive, self.my_send)

    async def my_receive(self):
        event = await self.receive()
        if event["type"] == "http.request" and self.is_request_json:
            self.request_body += event.get("body", b"")
            if not event.get("more_body", False):
                data = json.loads(self.request_body)
                print(f"request dump: {data}")

        return event

    async def my_send(self, event):
        if event["type"] == "http.response.start":
            headers = MutableHeaders(scope=event)
            self.is_response_json = is_json_content_type(headers.get("content-type"))

        elif event["type"] == "http.response.body" and self.is_response_json:
            self.response_body += event.get("body", b"")
            if not event.get("more_body", False):
                data = json.loads(self.response_body)
                print(f"response dump: {data}")

        await self.send(event)
