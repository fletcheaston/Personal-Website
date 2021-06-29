from typing import Any

from website.models import Project, Skill, WorkExperience
from website.utils import Server

from .base import templates


def home_template(
    *,
    projects: list[Project],
    server: Server,
) -> Any:
    return templates.TemplateResponse(
        "home.html",
        {
            "projects": projects,
            "request": server.request,
        },
    )


def about_template(
    *,
    skills: list[Skill],
    work_experiences: list[WorkExperience],
    server: Server,
) -> Any:
    return templates.TemplateResponse(
        "about.html",
        {
            "skills": skills,
            "work_experiences": work_experiences,
            "request": server.request,
        },
    )
