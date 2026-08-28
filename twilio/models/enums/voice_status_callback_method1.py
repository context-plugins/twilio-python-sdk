from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VoiceStatusCallbackMethod1(str, Enum):
    """The HTTP method we should use to call ``voice_status_callback_url``. Can be: ``GET`` or ``POST``."""

    GET = "GET"
    POST = "POST"

    __str__ = str.__str__


VoiceStatusCallbackMethod1OrStr: TypeAlias = Annotated[
    VoiceStatusCallbackMethod1 | str, open_enum_validator(VoiceStatusCallbackMethod1)
]
