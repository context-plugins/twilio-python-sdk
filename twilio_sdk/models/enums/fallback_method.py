from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FallbackMethod(str, Enum):
    """The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or ``POST`` and the default
    is ``POST``. If an ``application_sid`` parameter is present, this parameter is ignored."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


FallbackMethodOrStr: TypeAlias = Annotated[FallbackMethod | str, open_enum_validator(FallbackMethod)]
