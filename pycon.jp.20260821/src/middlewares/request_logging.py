from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middlewares.request_logging import RequestLoggingMiddleware

app = FastAPI()


@app.get("/logging")
@app.post("/logging")
async def index(request: Request) -> JSONResponse:
    print(f"{await request.body()=}")
    return JSONResponse({"message": "ok"})


app.add_middleware(RequestLoggingMiddleware)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
