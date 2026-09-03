from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomEnumRoomType(str, Enum):
    """Type of room. Use ``group`` for new implementations. ``go``, ``peer-to-peer``, and ``group-small`` are
    deprecated."""

    GROUP = "group"
    GO = "go"
    PEER_TO_PEER = "peer-to-peer"
    GROUP_SMALL = "group-small"

    __str__ = str.__str__


RoomEnumRoomTypeOrStr: TypeAlias = Annotated[RoomEnumRoomType | str, open_enum_validator(RoomEnumRoomType)]
