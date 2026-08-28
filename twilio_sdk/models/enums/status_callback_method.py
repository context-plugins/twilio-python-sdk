from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod(str, Enum):
    """The HTTP method we use to call ``status_callback``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethodOrStr: TypeAlias = Annotated[StatusCallbackMethod | str, open_enum_validator(StatusCallbackMethod)]
