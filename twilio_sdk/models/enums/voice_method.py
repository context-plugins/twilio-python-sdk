from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceMethod(str, Enum):
    """The HTTP method we use to call ``voice_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceMethodOrStr: TypeAlias = Annotated[VoiceMethod | str, open_enum_validator(VoiceMethod)]
