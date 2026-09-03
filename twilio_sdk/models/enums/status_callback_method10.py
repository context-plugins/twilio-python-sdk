from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod10(str, Enum):
    """The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or ``POST`` and defaults to
    ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethod10OrStr: TypeAlias = Annotated[
    StatusCallbackMethod10 | str, open_enum_validator(StatusCallbackMethod10)
]
