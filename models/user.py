from pydantic import BaseModel

from datetime import datetime


class LoginForm(BaseModel):
    phone: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    expiry: datetime


class UserCreateForm(BaseModel):
    name: str
    phone: str
    role: str = "USER"
    password: str


class UserUpdateForm(BaseModel):
    name: str = None


class UserResponse(BaseModel):
    user_id: str
    name: str
    phone: str
    role: str
