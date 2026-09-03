from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Method2(str, Enum):
    """How to pass the update request data. Can be ``GET`` or ``POST`` and the default is ``POST``. ``POST`` sends the
    data as encoded form data and ``GET`` sends the data as query parameters."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


Method2OrStr: TypeAlias = Annotated[Method2 | str, open_enum_validator(Method2)]
