from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoParticipantSummaryEnumRoomStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    CONNECTED = "connected"
    COMPLETED = "completed"
    DISCONNECTED = "disconnected"

    __str__ = str.__str__


VideoParticipantSummaryEnumRoomStatusOrStr: TypeAlias = Annotated[
    VideoParticipantSummaryEnumRoomStatus | str, open_enum_validator(VideoParticipantSummaryEnumRoomStatus)
]
