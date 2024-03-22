from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AUTH_SERVICE_URL: str = "http://127.0.0.1:8080/v1"
    OAUTH_SERVICE_URL: str = "http://127.0.0.1:8080/oauth"
    BOOKING_SERVICE_URL: str = "http://127.0.0.1:8081/v1"
    ROOM_SERVICE_URL: str = "http://127.0.0.1:8082/v1"


settings = Settings()
