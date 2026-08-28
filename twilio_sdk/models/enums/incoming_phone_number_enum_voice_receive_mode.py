from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomingPhoneNumberEnumVoiceReceiveMode(str, Enum):
    VOICE = "voice"
    FAX = "fax"

    __str__ = str.__str__


IncomingPhoneNumberEnumVoiceReceiveModeOrStr: TypeAlias = Annotated[
    IncomingPhoneNumberEnumVoiceReceiveMode | str, open_enum_validator(IncomingPhoneNumberEnumVoiceReceiveMode)
]
