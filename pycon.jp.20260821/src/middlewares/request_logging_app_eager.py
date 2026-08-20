from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middlewares.request_logging_app_eager import RequestLoggingMiddleware

app = FastAPI()
app.add_middleware(RequestLoggingMiddleware)


@app.post("/logging")
async def index(request: Request) -> JSONResponse:
    print(f"{await request.body()=}")
    return JSONResponse({"message": "ok"})

@app.post("/logging/not_use_body")
async def index(request: Request) -> JSONResponse:
    return JSONResponse({"message": "ok"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
