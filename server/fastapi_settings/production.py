from typing import List

from .base import Settings as BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False

    CORS_ORIGINS: List[str] = [
        "https://fletcheaston.com",
    ]

    # Unused
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = ""
    DATABASE_HOST: str = "localhost"
    DATABASE_NAME: str = "postgres"
