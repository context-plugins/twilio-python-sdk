from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomRecordingEnumType(str, Enum):
    """The recording's media type. Can be: ``audio`` or ``video``."""

    AUDIO = "audio"
    VIDEO = "video"
    DATA = "data"

    __str__ = str.__str__


RoomRecordingEnumTypeOrStr: TypeAlias = Annotated[
    RoomRecordingEnumType | str, open_enum_validator(RoomRecordingEnumType)
]
