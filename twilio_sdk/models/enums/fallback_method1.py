from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FallbackMethod1(str, Enum):
    """The HTTP method for the fallback webhook."""

    POST = "POST"
    PUT = "PUT"

    __str__ = str.__str__


FallbackMethod1OrStr: TypeAlias = Annotated[FallbackMethod1 | str, open_enum_validator(FallbackMethod1)]
