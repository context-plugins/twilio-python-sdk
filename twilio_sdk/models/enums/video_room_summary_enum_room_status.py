from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoRoomSummaryEnumRoomStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

    __str__ = str.__str__


VideoRoomSummaryEnumRoomStatusOrStr: TypeAlias = Annotated[
    VideoRoomSummaryEnumRoomStatus | str, open_enum_validator(VideoRoomSummaryEnumRoomStatus)
]
