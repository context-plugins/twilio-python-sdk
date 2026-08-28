from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomingPhoneNumberLocalEnumVoiceReceiveMode(str, Enum):
    VOICE = "voice"
    FAX = "fax"

    __str__ = str.__str__


IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr: TypeAlias = Annotated[
    IncomingPhoneNumberLocalEnumVoiceReceiveMode | str,
    open_enum_validator(IncomingPhoneNumberLocalEnumVoiceReceiveMode),
]
