from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SessionEnumMode(str, Enum):
    """The Mode of the Session. Can be: ``message-only``, ``voice-only``, or ``voice-and-message``."""

    MESSAGE_ONLY = "message-only"
    VOICE_ONLY = "voice-only"
    VOICE_AND_MESSAGE = "voice-and-message"

    __str__ = str.__str__


SessionEnumModeOrStr: TypeAlias = Annotated[SessionEnumMode | str, open_enum_validator(SessionEnumMode)]
