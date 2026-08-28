from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeauthorizeCallbackMethod(str, Enum):
    """The HTTP method we use to call ``deauthorize_callback_url``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


DeauthorizeCallbackMethodOrStr: TypeAlias = Annotated[
    DeauthorizeCallbackMethod | str, open_enum_validator(DeauthorizeCallbackMethod)
]
