from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoRoomSummaryEnumProcessingState(str, Enum):
    COMPLETE = "complete"
    IN_PROGRESS = "in_progress"
    TIMEOUT = "timeout"
    NOT_STARTED = "not_started"

    __str__ = str.__str__


VideoRoomSummaryEnumProcessingStateOrStr: TypeAlias = Annotated[
    VideoRoomSummaryEnumProcessingState | str, open_enum_validator(VideoRoomSummaryEnumProcessingState)
]
