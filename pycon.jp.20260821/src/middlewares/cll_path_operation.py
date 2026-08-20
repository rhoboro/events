# uv run cll_path_operation.py
# curl http://127.0.0.1:8000/cll/users/123
import asyncio
import logging
import random
import time
from typing import Annotated

from structlog import contextvars
from fastapi import Depends, FastAPI, Path, Request
from fastapi.responses import JSONResponse

from middlewares.canonical_log_line import CanonicalLogLine


app = FastAPI()
app.add_middleware(CanonicalLogLine)

UserId = Annotated[str, Path()]


async def bind_user_id(user_id: UserId) -> None:
    contextvars.bind_contextvars(user_id=user_id)


# 別スレッドで実行されるため、ミドルウェアと異なるコンテキストになる
@app.get(
    "/cll/users/{user_id}",
    dependencies=[Depends(bind_user_id)],
)
def get_user(request: Request, user_id: UserId) -> JSONResponse:
    items = random.randint(0, 100)
    contextvars.bind_contextvars(items=items)
    return JSONResponse({"user": user_id, "items": items})


if __name__ == "__main__":
    import structlog
    import uvicorn

    # https://www.structlog.org/en/stable/getting-started.html#getting-started
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False),
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=False,
    )

    uvicorn.run(app)
