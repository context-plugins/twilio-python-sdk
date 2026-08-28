from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RealtimeTranscriptionEnumStatus(str, Enum):
    """The status - one of ``stopped``, ``in-flight``"""

    IN_PROGRESS = "in-progress"
    STOPPED = "stopped"

    __str__ = str.__str__


RealtimeTranscriptionEnumStatusOrStr: TypeAlias = Annotated[
    RealtimeTranscriptionEnumStatus | str, open_enum_validator(RealtimeTranscriptionEnumStatus)
]
