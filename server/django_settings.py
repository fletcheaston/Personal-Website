from pathlib import Path
from typing import Any

from .config import settings

# We're a little deep into the filesystem, gotta point to where manage.py is.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key isn't actually used anywhere, FastAPI is handling all of the server security.
SECRET_KEY: str = "django-insecure"
DEBUG: bool = settings.DEBUG
BACKEND_CORS_ORIGINS: list[str] = settings.CORS_ORIGINS

# Postgres for our database, and our lone application.
INSTALLED_APPS: list[str] = [
    "django.contrib.postgres",
    "website.apps.WebsiteConfig",
]

DATABASES: dict[str, Any] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": settings.DATABASE_NAME,
        "USER": settings.DATABASE_USER,
        "PASSWORD": settings.DATABASE_PASSWORD,
        "HOST": settings.DATABASE_HOST,
        "PORT": settings.DATABASE_PORT,
    }
}

# Used to make Django happy.
DEFAULT_TABLESPACE: str = ""
ABSOLUTE_URL_OVERRIDES: dict[str, Any] = {}
DATABASE_ROUTERS: list[str] = []

# Internationalization, also required to make Django happy.
LANGUAGE_CODE: str = "en-us"
TIME_ZONE: str = "UTC"
USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True
