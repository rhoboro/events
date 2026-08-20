from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middlewares.authentication import UnauthorizedAuthentication, basic_auth

app = FastAPI()
app.add_middleware(UnauthorizedAuthentication, auth_backend=basic_auth)


@app.get("/auth")
async def index(request: Request) -> JSONResponse:
    return JSONResponse({"message": "ok"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
