from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoRoomSummaryEnumRoomType(str, Enum):
    GO = "go"
    PEER_TO_PEER = "peer_to_peer"
    GROUP = "group"
    GROUP_SMALL = "group_small"

    __str__ = str.__str__


VideoRoomSummaryEnumRoomTypeOrStr: TypeAlias = Annotated[
    VideoRoomSummaryEnumRoomType | str, open_enum_validator(VideoRoomSummaryEnumRoomType)
]
