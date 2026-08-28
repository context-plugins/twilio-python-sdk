from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomTranscriptionsEnumStatus(str, Enum):
    """The status of the transcriptions resource."""

    STARTED = "started"
    STOPPED = "stopped"
    FAILED = "failed"

    __str__ = str.__str__


RoomTranscriptionsEnumStatusOrStr: TypeAlias = Annotated[
    RoomTranscriptionsEnumStatus | str, open_enum_validator(RoomTranscriptionsEnumStatus)
]
