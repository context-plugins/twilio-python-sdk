from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeauthorizeCallbackMethod1(str, Enum):
    """The HTTP method to use when calling ``deauthorize_callback_url``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


DeauthorizeCallbackMethod1OrStr: TypeAlias = Annotated[
    DeauthorizeCallbackMethod1 | str, open_enum_validator(DeauthorizeCallbackMethod1)
]
