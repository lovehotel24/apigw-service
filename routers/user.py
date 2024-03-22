from fastapi import APIRouter, Request, status, Depends
from fastapi.security import HTTPBearer

from uuid import UUID

from service_router import service_route
from models.user import LoginForm, UserCreateForm, UserUpdateForm
from settings import settings

router = APIRouter(tags=["USER"])
security = HTTPBearer()


@service_route(
    request_method=router.post,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user/login",
    status_code=status.HTTP_200_OK,
    payload_key="login",
    response_model="models.user.LoginResponse",
)
async def login(login: LoginForm, request: Request):  # noqa
    """Login to the App"""
    ...


@service_route(
    request_method=router.post,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user/register",
    status_code=status.HTTP_200_OK,
    payload_key="register",
    response_model="models.user.UserResponse",
)
async def register(register: UserCreateForm, request: Request):  # noqa
    """Account Registration"""
    ...


@service_route(
    request_method=router.get,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user/logout",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    auth_required=True,
)
async def logout(request: Request, authorization: str = Depends(security)):  # noqa
    """Logout from the App"""
    ...


@service_route(
    request_method=router.get,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user/current_user",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    auth_required=True,
    response_model="models.user.UserResponse",
)
async def read_current_user(request: Request, authorization: str = Depends(security)):  # noqa
    """Read the Current User Information"""
    ...


@service_route(
    request_method=router.get,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    auth_required=True,
    admin_role_required=True,
    response_model="models.user.UserResponse",
)
async def read_all_users(request: Request, authorization: str = Depends(security)):  # noqa
    """Read All User Information"""
    ...


@service_route(
    request_method=router.get,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user/{user_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    auth_required=True,
    admin_role_required=True,
    response_model="models.user.UserResponse",
)
async def read_a_user(user_id: UUID, request: Request, authorization: str = Depends(security)):  # noqa
    """Read the Specific User Information"""
    ...


@service_route(
    request_method=router.put,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user/{user_id}",
    status_code=status.HTTP_200_OK,
    payload_key="user",
    auth_required=True,
    response_model="models.user.UserResponse",
)
async def update_a_user(user_id: UUID, user: UserUpdateForm, request: Request,  # noqa
                        authorization: str = Depends(security)):  # noqa
    """Update the Specific User Information"""
    ...


@service_route(
    request_method=router.delete,
    service_url=settings.AUTH_SERVICE_URL,
    path="/user/{user_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    auth_required=True,
    admin_role_required=True,
)
async def delete_a_user(user_id: UUID, request: Request, authorization: str = Depends(security)):  # noqa
    """Delete the Specific User"""
    ...
