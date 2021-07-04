from typing import Any

from website.models import Skill, WorkExperience
from website.utils import Server

from .base import templates


def home_template(
    *,
    skills: list[Skill],
    work_experiences: list[WorkExperience],
    server: Server,
) -> Any:
    return templates.TemplateResponse(
        "home.html",
        {
            "skills": skills,
            "work_experiences": work_experiences,
            "request": server.request,
        },
    )
