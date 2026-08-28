from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceEnumProcessingState(str, Enum):
    COMPLETE = "complete"
    IN_PROGRESS = "in_progress"
    TIMEOUT = "timeout"

    __str__ = str.__str__


ConferenceEnumProcessingStateOrStr: TypeAlias = Annotated[
    ConferenceEnumProcessingState | str, open_enum_validator(ConferenceEnumProcessingState)
]
