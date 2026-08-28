from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingEnumStatus(str, Enum):
    """The status of the recording. Can be: ``processing``, ``completed``, ``absent`` or ``deleted``. For information
    about more detailed statuses on in-progress recordings, check out how to `Update a Recording Resource
    <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__."""

    IN_PROGRESS = "in-progress"
    PAUSED = "paused"
    STOPPED = "stopped"
    PROCESSING = "processing"
    COMPLETED = "completed"
    ABSENT = "absent"
    DELETED = "deleted"

    __str__ = str.__str__


RecordingEnumStatusOrStr: TypeAlias = Annotated[RecordingEnumStatus | str, open_enum_validator(RecordingEnumStatus)]
