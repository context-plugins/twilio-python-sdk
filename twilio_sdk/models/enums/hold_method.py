from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HoldMethod(str, Enum):
    """The HTTP method we should use to call ``hold_url``. Can be: ``GET`` or ``POST`` and the default is ``GET``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


HoldMethodOrStr: TypeAlias = Annotated[HoldMethod | str, open_enum_validator(HoldMethod)]
