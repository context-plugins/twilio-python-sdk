from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceParticipantEnumProcessingState(str, Enum):
    COMPLETE = "complete"
    IN_PROGRESS = "in_progress"
    TIMEOUT = "timeout"

    __str__ = str.__str__


ConferenceParticipantEnumProcessingStateOrStr: TypeAlias = Annotated[
    ConferenceParticipantEnumProcessingState | str, open_enum_validator(ConferenceParticipantEnumProcessingState)
]
