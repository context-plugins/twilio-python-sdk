from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StreamEnumTrack(str, Enum):
    """The tracks to be included in the Stream. Possible values are ``inbound_track``, ``outbound_track``,
    ``both_tracks``. Default value is ``inbound_track``."""

    INBOUND_TRACK = "inbound_track"
    OUTBOUND_TRACK = "outbound_track"
    BOTH_TRACKS = "both_tracks"

    __str__ = str.__str__


StreamEnumTrackOrStr: TypeAlias = Annotated[StreamEnumTrack | str, open_enum_validator(StreamEnumTrack)]
