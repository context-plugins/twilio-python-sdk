from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsFallbackMethod6(str, Enum):
    """The HTTP method we use to call the ``sms_fallback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


SmsFallbackMethod6OrStr: TypeAlias = Annotated[SmsFallbackMethod6 | str, open_enum_validator(SmsFallbackMethod6)]
