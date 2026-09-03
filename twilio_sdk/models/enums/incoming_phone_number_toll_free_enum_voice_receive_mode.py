from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomingPhoneNumberTollFreeEnumVoiceReceiveMode(str, Enum):
    VOICE = "voice"
    FAX = "fax"

    __str__ = str.__str__


IncomingPhoneNumberTollFreeEnumVoiceReceiveModeOrStr: TypeAlias = Annotated[
    IncomingPhoneNumberTollFreeEnumVoiceReceiveMode | str,
    open_enum_validator(IncomingPhoneNumberTollFreeEnumVoiceReceiveMode),
]
