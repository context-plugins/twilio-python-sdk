from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingEnumStatus1(str, Enum):
    """The status of the recording. Can be: ``processing``, ``completed``, or ``deleted``. ``processing`` indicates the
    recording is still being captured; ``completed`` indicates the recording has been captured and is now available for
    download. ``deleted`` means the recording media has been deleted from the system, but its metadata is still
    available."""

    PROCESSING = "processing"
    COMPLETED = "completed"
    DELETED = "deleted"
    FAILED = "failed"

    __str__ = str.__str__


RecordingEnumStatus1OrStr: TypeAlias = Annotated[RecordingEnumStatus1 | str, open_enum_validator(RecordingEnumStatus1)]
