from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingEnumCodec(str, Enum):
    """The codec used to encode the track. Can be: ``VP8``, ``H264``, ``OPUS``, and ``PCMU``."""

    VP8 = "VP8"
    H264 = "H264"
    OPUS = "OPUS"
    PCMU = "PCMU"

    __str__ = str.__str__


RecordingEnumCodecOrStr: TypeAlias = Annotated[RecordingEnumCodec | str, open_enum_validator(RecordingEnumCodec)]
