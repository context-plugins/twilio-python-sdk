from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomRecordingEnumFormat(str, Enum):
    MKA = "mka"
    MKV = "mkv"

    __str__ = str.__str__


RoomRecordingEnumFormatOrStr: TypeAlias = Annotated[
    RoomRecordingEnumFormat | str, open_enum_validator(RoomRecordingEnumFormat)
]
