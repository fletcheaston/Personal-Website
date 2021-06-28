import os
from functools import lru_cache
from typing import Optional, Type

from .fastapi_settings.base import Settings as BaseSettings
from .fastapi_settings.local import Settings as LocalSettings


@lru_cache
def get_settings() -> BaseSettings:
    available_settings: dict[Optional[str], Type[BaseSettings]] = {
        None: LocalSettings,
        "local": LocalSettings,
        "fletcheaston-website": LocalSettings,
    }

    gcp_project = os.getenv("GOOGLE_CLOUD_PROJECT")

    return available_settings[gcp_project]()


settings: BaseSettings = get_settings()
