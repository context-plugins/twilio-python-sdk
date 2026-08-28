from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomingPhoneNumberMobileEnumVoiceReceiveMode(str, Enum):
    VOICE = "voice"
    FAX = "fax"

    __str__ = str.__str__


IncomingPhoneNumberMobileEnumVoiceReceiveModeOrStr: TypeAlias = Annotated[
    IncomingPhoneNumberMobileEnumVoiceReceiveMode | str,
    open_enum_validator(IncomingPhoneNumberMobileEnumVoiceReceiveMode),
]
