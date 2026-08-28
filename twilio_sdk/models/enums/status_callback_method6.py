from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod6(str, Enum):
    """The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethod6OrStr: TypeAlias = Annotated[
    StatusCallbackMethod6 | str, open_enum_validator(StatusCallbackMethod6)
]
