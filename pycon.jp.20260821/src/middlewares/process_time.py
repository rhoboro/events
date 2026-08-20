from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middlewares.process_time import ProcessTime

app = FastAPI()
app.add_middleware(ProcessTime)


@app.get("/")
async def index(request: Request) -> JSONResponse:
    return JSONResponse({"hello": "pyconjp"})


@app.get("/error")
async def index(request: Request) -> JSONResponse:
    raise RuntimeError("Panic")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
