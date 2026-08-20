# uv run canonical_log_line.py
# curl http://127.0.0.1:8000/users/123
import time
from uuid import uuid4
import structlog
from starlette.requests import Request


class CanonicalLogLine:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        start_time = time.perf_counter()
        request = Request(scope)
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            request_id=str(uuid4()),
            url=str(request.url),
        )

        await self.app(scope, receive, send)

        structlog.contextvars.bind_contextvars(
            processing_time=time.perf_counter() - start_time,
        )
        logger = structlog.get_logger()
        logger.info("canonical-log-line")
