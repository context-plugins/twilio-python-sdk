from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TranscriptionEnumStatus(str, Enum):
    """The status of the transcription. Can be: ``in-progress``, ``completed``, ``failed``."""

    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    FAILED = "failed"

    __str__ = str.__str__


TranscriptionEnumStatusOrStr: TypeAlias = Annotated[
    TranscriptionEnumStatus | str, open_enum_validator(TranscriptionEnumStatus)
]
