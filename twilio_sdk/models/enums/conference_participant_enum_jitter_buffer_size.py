from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceParticipantEnumJitterBufferSize(str, Enum):
    LARGE = "large"
    SMALL = "small"
    MEDIUM = "medium"
    OFF = "off"

    __str__ = str.__str__


ConferenceParticipantEnumJitterBufferSizeOrStr: TypeAlias = Annotated[
    ConferenceParticipantEnumJitterBufferSize | str, open_enum_validator(ConferenceParticipantEnumJitterBufferSize)
]
