from django.apps import AppConfig


class WebsiteConfig(AppConfig):  # type: ignore
    name = "website"

    def ready(self) -> None:
        from server.urls import router as server_router

        from .app import router as app_router

        server_router.include_router(app_router)
