# uv run process_time.py
# curl http://127.0.0.1:8000
# curl http://127.0.0.1:8000/error
import time
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def process_time() -> Iterator[None]:
    start_time = time.perf_counter()
    try:
        yield
    finally:
        process_time = time.perf_counter() - start_time
        print(f"processing time: {process_time}")


class ProcessTime:
    def __init__(self, app) -> None:
        self.app = app

    async def __call__(self, scope, receive, send):
        with process_time():
            await self.app(scope, receive, send)
