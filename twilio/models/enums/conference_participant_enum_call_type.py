from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceParticipantEnumCallType(str, Enum):
    CARRIER = "carrier"
    CLIENT = "client"
    SIP = "sip"

    __str__ = str.__str__


ConferenceParticipantEnumCallTypeOrStr: TypeAlias = Annotated[
    ConferenceParticipantEnumCallType | str, open_enum_validator(ConferenceParticipantEnumCallType)
]
