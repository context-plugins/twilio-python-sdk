from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceMethod7(str, Enum):
    """The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceMethod7OrStr: TypeAlias = Annotated[VoiceMethod7 | str, open_enum_validator(VoiceMethod7)]
