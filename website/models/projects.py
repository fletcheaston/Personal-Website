from .base import BaseModel


class Project(BaseModel):
    uid: str
    name: str
    description: str

    # DANGER: This attribute should be tested thoroughly before being used. Arbitrary HTML execution in Jinja2 is unsafe.
    html_content: str = "<div>No content</div>"
