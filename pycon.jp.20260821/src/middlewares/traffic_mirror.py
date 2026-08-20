from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middlewares.traffic_mirror import TrafficMirrorMiddleware

app = FastAPI()
app.add_middleware(TrafficMirrorMiddleware, base_url="https://api.rhoboro.com/echo/")


@app.post("/users/{user_id}")
async def index(request: Request) -> JSONResponse:
    return JSONResponse({"hello": "world"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
