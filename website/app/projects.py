from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from website.controllers import list_projects, list_skills, list_work_experiences
from website.templates import about_template, home_template
from website.utils import Server

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(server: Server = Depends()) -> Any:
    return home_template(
        projects=list_projects(),
        server=server,
    )


@router.get("/about", response_class=HTMLResponse)
def about(server: Server = Depends()) -> Any:
    return about_template(
        skills=list_skills(),
        work_experiences=list_work_experiences(),
        server=server,
    )
