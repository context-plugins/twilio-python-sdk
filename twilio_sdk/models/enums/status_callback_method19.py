from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCallbackMethod19(str, Enum):
    """The HTTP method Twilio uses when sending ``status_callback`` requests. Possible values are ``GET`` and ``POST``.
    Default is ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


StatusCallbackMethod19OrStr: TypeAlias = Annotated[
    StatusCallbackMethod19 | str, open_enum_validator(StatusCallbackMethod19)
]
