from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod17(str, Enum):
    """The http method for the status_callback (one of GET, POST)."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethod17OrStr: TypeAlias = Annotated[
    StatusCallbackMethod17 | str, open_enum_validator(StatusCallbackMethod17)
]
