from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoParticipantSummaryEnumCodec(str, Enum):
    VP8 = "VP8"
    H264 = "H264"
    VP9 = "VP9"
    OPUS = "opus"

    __str__ = str.__str__


VideoParticipantSummaryEnumCodecOrStr: TypeAlias = Annotated[
    VideoParticipantSummaryEnumCodec | str, open_enum_validator(VideoParticipantSummaryEnumCodec)
]
