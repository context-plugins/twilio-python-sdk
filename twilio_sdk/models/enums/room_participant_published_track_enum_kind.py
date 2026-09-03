from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomParticipantPublishedTrackEnumKind(str, Enum):
    """The track type. Can be: ``audio``, ``video`` or ``data``."""

    AUDIO = "audio"
    VIDEO = "video"
    DATA = "data"

    __str__ = str.__str__


RoomParticipantPublishedTrackEnumKindOrStr: TypeAlias = Annotated[
    RoomParticipantPublishedTrackEnumKind | str, open_enum_validator(RoomParticipantPublishedTrackEnumKind)
]
