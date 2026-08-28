from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsFallbackMethod14(str, Enum):
    """The HTTP method that we should use to call the ``sms_fallback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsFallbackMethod14OrStr: TypeAlias = Annotated[SmsFallbackMethod14 | str, open_enum_validator(SmsFallbackMethod14)]
