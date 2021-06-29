import inspect
from enum import Enum
from types import FunctionType
from typing import Dict, Type

from fastapi import (  # noqa
    BackgroundTasks,
    Form,
    HTTPException,
    Query,
    Request,
    Response,
)
from humps import camelize
from pydantic import ValidationError, dataclasses, validator  # noqa

from website.models.base import BaseModel


class Style(str, Enum):
    # These should have the same names as the CSS files in the styles directory.
    NEUMORPHISM = "neumorphism"
    TERMINAL = "terminal"
    SAM = "sam"


class Server(BaseModel):
    request: Request
    response: Response
    background: BackgroundTasks
    style: str = ""

    @validator("style", pre=True, always=True)
    def parse_style(cls, v: str) -> Style:
        styles: dict[str, Style] = {style.lower(): style for style in Style}
        return styles.get(v.lower(), Style.NEUMORPHISM)


#######################################################################################################################
# Schema input manipulation. Very hacky, but it generates nice docs.
# TODO: I've seen some examples that don't use this hacky method, should check out later.
# Copied from https://github.com/tiangolo/fastapi/issues/318#issuecomment-691121286
def as_query(name: str, model_cls: Type[BaseModel]) -> FunctionType:
    """
    Takes a pydantic model class as input and creates a dependency with corresponding
    Query parameter definitions that can be used for GET requests.

    This will only work, if the fields defined in the input model can be turned into
    suitable query parameters. Otherwise fastapi will complain down the road.

    Arguments:
        name: Name for the dependency function.
        model_cls: A ``BaseModel`` inheriting model class as input.
    """
    names = []
    annotations: Dict[str, type] = {}
    defaults = []
    for field_model in model_cls.__fields__.values():
        field_info = field_model.field_info

        field_name = camelize(field_model.name)
        names.append(field_name)
        annotations[field_name] = field_model.outer_type_
        defaults.append(Query(field_model.default, description=field_info.description))

    code = inspect.cleandoc(
        """
    def %s(%s):
        try:
            return %s(%s)
        except ValidationError as e:
            errors = e.errors()
            for error in errors:
                error['loc'] = ['query'] + list(error['loc'])
            raise HTTPException(422, detail=errors)

    """
        % (
            name,
            ", ".join(names),
            model_cls.__name__,
            ", ".join(["%s=%s" % (name, name) for name in names]),
        )
    )

    compiled = compile(code, "string", "exec")
    env = {model_cls.__name__: model_cls}
    env.update(**globals())
    func = FunctionType(compiled.co_consts[0], env, name)
    func.__annotations__ = annotations
    func.__defaults__ = (*defaults,)

    return func


def as_form(name: str, model_cls: Type[BaseModel]) -> FunctionType:
    """
    Takes a pydantic model class as input and creates a dependency with corresponding
    Form parameter definitions that can be used for POST requests.

    This will only work, if the fields defined in the input model can be turned into
    suitable form parameters. Otherwise fastapi will complain down the road.

    Arguments:
        name: Name for the dependency function.
        model_cls: A ``BaseModel`` inheriting model class as input.
    """
    names = []
    annotations: Dict[str, type] = {}
    defaults = []
    for field_model in model_cls.__fields__.values():
        field_info = field_model.field_info

        field_name = camelize(field_model.name)
        names.append(field_name)
        annotations[field_name] = field_model.outer_type_
        defaults.append(Form(field_model.default, description=field_info.description))

    code = inspect.cleandoc(
        """
    def %s(%s):
        try:
            return %s(%s)
        except ValidationError as e:
            errors = e.errors()
            for error in errors:
                error['loc'] = ['form'] + list(error['loc'])
            raise HTTPException(422, detail=errors)

    """
        % (
            name,
            ", ".join(names),
            model_cls.__name__,
            ", ".join(["%s=%s" % (name, name) for name in names]),
        )
    )

    compiled = compile(code, "string", "exec")
    env = {model_cls.__name__: model_cls}
    env.update(**globals())
    func = FunctionType(compiled.co_consts[0], env, name)
    func.__annotations__ = annotations
    func.__defaults__ = (*defaults,)

    return func
