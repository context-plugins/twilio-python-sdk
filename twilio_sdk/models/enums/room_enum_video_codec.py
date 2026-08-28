from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomEnumVideoCodec(str, Enum):
    VP8 = "VP8"
    H264 = "H264"

    __str__ = str.__str__


RoomEnumVideoCodecOrStr: TypeAlias = Annotated[RoomEnumVideoCodec | str, open_enum_validator(RoomEnumVideoCodec)]
