from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallRecordingEnumStatus(str, Enum):
    """The status of the recording. Can be: ``processing``, ``completed`` and ``absent``. For more detailed statuses on
    in-progress recordings, check out how to `Update a Recording Resource
    <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__."""

    IN_PROGRESS = "in-progress"
    PAUSED = "paused"
    STOPPED = "stopped"
    PROCESSING = "processing"
    COMPLETED = "completed"
    ABSENT = "absent"

    __str__ = str.__str__


CallRecordingEnumStatusOrStr: TypeAlias = Annotated[
    CallRecordingEnumStatus | str, open_enum_validator(CallRecordingEnumStatus)
]
