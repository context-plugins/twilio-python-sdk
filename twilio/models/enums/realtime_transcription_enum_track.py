from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RealtimeTranscriptionEnumTrack(str, Enum):
    """One of ``inbound_track``, ``outbound_track``, ``both_tracks``."""

    INBOUND_TRACK = "inbound_track"
    OUTBOUND_TRACK = "outbound_track"
    BOTH_TRACKS = "both_tracks"

    __str__ = str.__str__


RealtimeTranscriptionEnumTrackOrStr: TypeAlias = Annotated[
    RealtimeTranscriptionEnumTrack | str, open_enum_validator(RealtimeTranscriptionEnumTrack)
]
