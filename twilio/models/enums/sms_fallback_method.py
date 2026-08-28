from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsFallbackMethod(str, Enum):
    """The HTTP method we use to call ``sms_fallback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsFallbackMethodOrStr: TypeAlias = Annotated[SmsFallbackMethod | str, open_enum_validator(SmsFallbackMethod)]
