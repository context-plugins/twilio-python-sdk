from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceParticipantEnumCallDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    __str__ = str.__str__


ConferenceParticipantEnumCallDirectionOrStr: TypeAlias = Annotated[
    ConferenceParticipantEnumCallDirection | str, open_enum_validator(ConferenceParticipantEnumCallDirection)
]
