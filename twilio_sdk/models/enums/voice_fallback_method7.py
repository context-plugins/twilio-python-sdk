from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceFallbackMethod7(str, Enum):
    """The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceFallbackMethod7OrStr: TypeAlias = Annotated[VoiceFallbackMethod7 | str, open_enum_validator(VoiceFallbackMethod7)]
