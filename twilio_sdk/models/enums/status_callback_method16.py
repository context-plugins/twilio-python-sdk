from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod16(str, Enum):
    """The HTTP method we should use to call ``status_callback``. Can be: ``GET`` and ``POST`` and defaults to
    ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethod16OrStr: TypeAlias = Annotated[
    StatusCallbackMethod16 | str, open_enum_validator(StatusCallbackMethod16)
]
