from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod15(str, Enum):
    """The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or ``POST``, and the default is
    ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethod15OrStr: TypeAlias = Annotated[
    StatusCallbackMethod15 | str, open_enum_validator(StatusCallbackMethod15)
]
