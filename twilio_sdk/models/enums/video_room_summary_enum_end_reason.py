from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoRoomSummaryEnumEndReason(str, Enum):
    ROOM_ENDED_VIA_API = "room_ended_via_api"
    TIMEOUT = "timeout"

    __str__ = str.__str__


VideoRoomSummaryEnumEndReasonOrStr: TypeAlias = Annotated[
    VideoRoomSummaryEnumEndReason | str, open_enum_validator(VideoRoomSummaryEnumEndReason)
]
