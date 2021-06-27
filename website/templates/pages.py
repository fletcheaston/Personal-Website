from typing import Any

from website.utils import Server

from .base import templates


def home_template(*, server: Server) -> Any:
    return templates.TemplateResponse(
        "home.html",
        {
            "request": server.request,
        },
    )


def about_template(*, server: Server) -> Any:
    return templates.TemplateResponse(
        "about.html",
        {
            "request": server.request,
        },
    )
