from pydantic_settings import BaseSettings

import secrets
from typing import Literal


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"


settings = Settings()
