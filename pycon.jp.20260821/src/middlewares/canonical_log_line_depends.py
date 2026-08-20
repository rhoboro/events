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


# 別スレッドで実行されるため、ミドルウェアと異なるコンテキストになる
async def bind_user_id(user_id: UserId) -> None:
    contextvars.bind_contextvars(user_id=user_id)


@app.get(
    "/users/{user_id}",
    dependencies=[Depends(bind_user_id)],
)
async def get_user(request: Request, user_id: UserId) -> JSONResponse:
    sleep_time = random.random()
    await asyncio.sleep(sleep_time)
    contextvars.bind_contextvars(sleep_time=sleep_time)
    return JSONResponse({"user": user_id})


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
