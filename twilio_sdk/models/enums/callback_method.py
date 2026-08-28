from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallbackMethod(str, Enum):
    """The HTTP method we use to call ``callback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


CallbackMethodOrStr: TypeAlias = Annotated[CallbackMethod | str, open_enum_validator(CallbackMethod)]
