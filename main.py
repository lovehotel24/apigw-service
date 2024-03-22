""""
from pydantic import BaseModel


class TestInput(BaseModel):
    name: str
    age: int

# mock
@app.get("/service/test/{test_id}")
def test_service(test_id: int):
    return {"data": {"test_id": test_id}}


# mock payload
@app.post("/service/test/{test_id}")
def test_payload_service(test_id: int, data: TestInput):
    return {"data": {"test_id": test_id, "response_data": data}}


# w/o payload
@route(
    request_method=app.get,
    service_url="http://127.0.0.1:8000/service",
    path="/test/{test_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None)
async def test(test_id: int, request: Request):  # noqa
    pass


# w/ payload
@route(
    request_method=app.post,
    service_url="http://127.0.0.1:8000/service",
    path="/test/{test_id}",
    status_code=status.HTTP_200_OK,
    payload_key="test")
async def test_payload(test_id: int, test: TestInput, request: Request):  # noqa
    pass
"""

import uvicorn
from fastapi import FastAPI

# APIRouters
from routers.user import router as auth_router
from routers.booking import router as booking_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(booking_router)


@app.get("/health", tags=["HEALTH"])
def health_check():
    """Health Check of All Microservices"""

    return {"status": "up"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8008,
        reload=True,
        server_header=False,
    )
