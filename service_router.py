from functools import wraps
from importlib import import_module

from fastapi import Request, HTTPException

from service_dealer import ServiceDealer
from auth import validate_access_token


def service_route(
        request_method,
        service_url: str,
        path: str,
        status_code: int,
        payload_key: str | None,
        auth_required: bool = False,
        admin_role_required: bool = False,
        response_model: str | None = None,
):
    """Service Route to the Respective Microservice"""

    app_method = request_method(
        path=path,
        status_code=status_code,
        response_model=import_model(response_model)
    )

    def wrapper(f):
        @app_method
        @wraps(f)
        async def inner_func(request: Request, **kwargs):
            service_headers = {}

            if auth_required:
                # If the user needs to be authenticated, validate its access token.
                authorization = request.headers.get("authorization")
                validation_result = await validate_access_token(authorization)

                if "user_id" in validation_result.keys():
                    service_headers = {"Authorization": authorization}

                # Todo: WIP
                if admin_role_required:
                    # This will check whether the user has admin access or not.
                    is_eligible = True
                    if is_eligible:
                        pass

            scope = request.scope
            method = scope["method"].lower()

            url = f"{service_url}{scope['path']}"

            payload_obj = kwargs.get(payload_key)
            payload_data = payload_obj.dict() if payload_obj else {}

            # This will send an API request to the microservice destination.
            service_dealer = ServiceDealer(
                url=url,
                method=method,
                headers=service_headers,
                data=payload_data,
            )
            service_resp_data, service_resp_status_code = await service_dealer.fetch_api()

            # If the response status code is not the desired code, raise as an error.
            if status_code == service_resp_status_code:
                return service_resp_data
            else:
                raise HTTPException(
                    status_code=service_resp_status_code,
                    detail=service_resp_data,
                    headers={'WWW-Authenticate': 'Bearer'},
                )

    return wrapper


def import_model(module_info):
    """Helper Func to Import Pydantic Data Model"""

    if module_info:
        module, model = module_info.rsplit(".", 1)
        module = import_module(module)
        return getattr(module, model)
