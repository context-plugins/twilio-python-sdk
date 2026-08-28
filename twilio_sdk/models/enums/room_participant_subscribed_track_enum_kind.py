from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomParticipantSubscribedTrackEnumKind(str, Enum):
    """The track type. Can be: ``audio``, ``video`` or ``data``."""

    AUDIO = "audio"
    VIDEO = "video"
    DATA = "data"

    __str__ = str.__str__


RoomParticipantSubscribedTrackEnumKindOrStr: TypeAlias = Annotated[
    RoomParticipantSubscribedTrackEnumKind | str, open_enum_validator(RoomParticipantSubscribedTrackEnumKind)
]
