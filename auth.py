from fastapi import HTTPException, status

from settings import settings
from service_dealer import ServiceDealer


async def validate_access_token(authorization: str):
    """Access Token Validation with Auth Service"""

    oauth_service_url = settings.OAUTH_SERVICE_URL

    access_token = authorization.replace('Bearer ', '')
    url = f"{oauth_service_url}/validate_token?access_token={access_token}"

    service_dealer = ServiceDealer(
        url=url,
        method="get",
        data={},
        headers={},
    )
    service_resp_data, service_resp_status_code = await service_dealer.fetch_api()

    if service_resp_status_code == 200:
        return service_resp_data
    else:
        raise HTTPException(
            status_code=service_resp_status_code,
            detail=service_resp_data,
            headers={'WWW-Authenticate': 'Bearer'},
        )
