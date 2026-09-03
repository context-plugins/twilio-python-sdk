from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Method3(str, Enum):
    """The HTTP method Twilio will use when requesting the above ``Url``. Either ``GET`` or ``POST``. Default is
    ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


Method3OrStr: TypeAlias = Annotated[Method3 | str, open_enum_validator(Method3)]
