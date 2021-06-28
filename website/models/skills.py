from .base import BaseModel


class Skill(BaseModel):
    category: str
    technologies: list[str]
