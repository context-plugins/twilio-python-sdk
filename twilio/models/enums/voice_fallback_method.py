from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceFallbackMethod(str, Enum):
    """The HTTP method we use to call ``voice_fallback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceFallbackMethodOrStr: TypeAlias = Annotated[VoiceFallbackMethod | str, open_enum_validator(VoiceFallbackMethod)]
