import aiohttp
from fastapi import HTTPException, status


class ServiceDealer:
    def __init__(
            self,
            url: str,
            method: str,
            headers: dict,
            data: dict,
    ):
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data

    async def _send_request(self):
        async with aiohttp.ClientSession() as session:
            request = getattr(session, self.method)
            async with request(self.url, headers=self.headers, json=self.data) as resp:
                data = await resp.json()
                return data, resp.status

    async def fetch_api(self):
        try:
            service_resp_data, service_resp_status_code = await self._send_request()
            return service_resp_data, service_resp_status_code
        except aiohttp.client_exceptions.ClientConnectorError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="service is unavailable",
                headers={'WWW-Authenticate': 'Bearer'},
            )
        except aiohttp.client_exceptions.ContentTypeError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="service seems to have error",
                headers={'WWW-Authenticate': 'Bearer'},
            )
