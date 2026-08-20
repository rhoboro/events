from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middlewares.health_check import HealthCheck

app = FastAPI()
app.add_middleware(HealthCheck)


@app.get("/")
async def index(request: Request) -> JSONResponse:
    return JSONResponse({"hello": "pyconjp"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
