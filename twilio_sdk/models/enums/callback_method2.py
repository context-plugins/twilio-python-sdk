from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallbackMethod2(str, Enum):
    """The HTTP method for the webhook."""

    POST = "POST"
    PUT = "PUT"

    __str__ = str.__str__


CallbackMethod2OrStr: TypeAlias = Annotated[CallbackMethod2 | str, open_enum_validator(CallbackMethod2)]
