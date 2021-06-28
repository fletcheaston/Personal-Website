from .base import BaseModel


class Accomplishment(BaseModel):
    description: str


class WorkExperience(BaseModel):
    title: str
    company: str
    start_date: str
    end_date: str
    accomplishments: list[Accomplishment]
