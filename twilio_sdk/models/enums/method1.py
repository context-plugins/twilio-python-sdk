from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Method1(str, Enum):
    """The HTTP method we should use when calling the ``url``. Can be: ``GET`` or ``POST`` and the default is ``POST``.
    If an ``application_sid`` parameter is present, this parameter is ignored."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


Method1OrStr: TypeAlias = Annotated[Method1 | str, open_enum_validator(Method1)]
