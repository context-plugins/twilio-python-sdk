from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceStatusCallbackMethod(str, Enum):
    """The HTTP method we use to call ``voice_status_callback_url``. Either ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceStatusCallbackMethodOrStr: TypeAlias = Annotated[
    VoiceStatusCallbackMethod | str, open_enum_validator(VoiceStatusCallbackMethod)
]
