from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomRecordingEnumStatus(str, Enum):
    """The status of the recording. Can be: ``processing``, ``completed``, or ``deleted``. ``processing`` indicates the
    Recording is still being captured. ``completed`` indicates the Recording has been captured and is now available for
    download. ``deleted`` means the recording media has been deleted from the system, but its metadata is still
    available for historical purposes."""

    PROCESSING = "processing"
    COMPLETED = "completed"
    DELETED = "deleted"
    FAILED = "failed"

    __str__ = str.__str__


RoomRecordingEnumStatusOrStr: TypeAlias = Annotated[
    RoomRecordingEnumStatus | str, open_enum_validator(RoomRecordingEnumStatus)
]
