from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsFallbackMethod7(str, Enum):
    """The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsFallbackMethod7OrStr: TypeAlias = Annotated[SmsFallbackMethod7 | str, open_enum_validator(SmsFallbackMethod7)]
