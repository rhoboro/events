# uv run uvicorn process_time:app
# curl http://127.0.0.1:8000
import time

from asgi_app import AsgiApp
from asgi_middleware import AsgiMiddleware


class ProcessTime:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        start_time = time.perf_counter()
        await self.app(scope, receive, send)
        process_time = time.perf_counter() - start_time
        print(f"processing time: {process_time}")


app = ProcessTime(AsgiMiddleware(AsgiApp()))
# app = AsgiMiddleware(ProcessTime(AsgiApp()))
