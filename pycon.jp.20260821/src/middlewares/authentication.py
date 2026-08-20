from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from middlewares.authentication import Authentication, basic_auth

app = FastAPI()
app.add_middleware(Authentication, auth_backend=basic_auth)


@app.get("/")
async def index(request: Request) -> JSONResponse:
    return JSONResponse({"user": request.state.user})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
