from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordingTranscriptionEnumStatus(str, Enum):
    """The status of the transcription. Can be: ``in-progress``, ``completed``, ``failed``."""

    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    FAILED = "failed"

    __str__ = str.__str__


RecordingTranscriptionEnumStatusOrStr: TypeAlias = Annotated[
    RecordingTranscriptionEnumStatus | str, open_enum_validator(RecordingTranscriptionEnumStatus)
]
