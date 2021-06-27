from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from website.templates import about_template, home_template
from website.utils import Server

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(server: Server = Depends()) -> Any:
    return home_template(server=server)


@router.get("/about", response_class=HTMLResponse)
def about(server: Server = Depends()) -> Any:
    return about_template(server=server)
