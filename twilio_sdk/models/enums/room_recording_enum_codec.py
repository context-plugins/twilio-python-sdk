from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomRecordingEnumCodec(str, Enum):
    """The codec used for the recording. Can be: ``VP8`` or ``H264``."""

    VP8 = "VP8"
    H264 = "H264"
    OPUS = "OPUS"
    PCMU = "PCMU"

    __str__ = str.__str__


RoomRecordingEnumCodecOrStr: TypeAlias = Annotated[
    RoomRecordingEnumCodec | str, open_enum_validator(RoomRecordingEnumCodec)
]
