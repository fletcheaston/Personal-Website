import logging

from django.apps import apps
from django.conf import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_restful.timing import add_timing_middleware

from server import django_settings as server_settings
from server.urls import router

try:
    settings.configure(server_settings)
except RuntimeError:  # Avoid: "Settings already configured."
    pass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


apps.populate(settings.INSTALLED_APPS)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    "/static",
    StaticFiles(directory="website/templates/static"),
    name="static",
)
app.include_router(router)
add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
