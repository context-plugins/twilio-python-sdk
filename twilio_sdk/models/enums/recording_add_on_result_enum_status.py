from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingAddOnResultEnumStatus(str, Enum):
    """The status of the result. Can be: ``canceled``, ``completed``, ``deleted``, ``failed``, ``in-progress``,
    ``init``, ``processing``, ``queued``."""

    CANCELED = "canceled"
    COMPLETED = "completed"
    DELETED = "deleted"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    INIT = "init"
    PROCESSING = "processing"
    QUEUED = "queued"

    __str__ = str.__str__


RecordingAddOnResultEnumStatusOrStr: TypeAlias = Annotated[
    RecordingAddOnResultEnumStatus | str, open_enum_validator(RecordingAddOnResultEnumStatus)
]
