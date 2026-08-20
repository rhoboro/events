# uv run request_logging.py
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
        request_body = b""

        async def my_receive():
            nonlocal request_body
            event = await receive()
            if event["type"] == "http.request" and is_request_json:
                request_body += event.get("body", b"")
                if not event.get("more_body", False):
                    data = json.loads(request_body)
                    print(f"request dump: {data}")

            return event

        is_response_json = False
        response_body = b""

        async def my_send(event):
            nonlocal is_response_json, response_body
            if event["type"] == "http.response.start":
                headers = MutableHeaders(scope=event)
                is_response_json = is_json_content_type(headers.get("content-type"))

            elif event["type"] == "http.response.body" and is_response_json:
                response_body += event.get("body", b"")
                if not event.get("more_body", False):
                    data = json.loads(response_body)
                    print(f"response dump: {data}")

            await send(event)

        await self.app(scope, my_receive, my_send)
