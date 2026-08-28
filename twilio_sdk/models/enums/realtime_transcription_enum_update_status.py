from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RealtimeTranscriptionEnumUpdateStatus(str, Enum):
    STOPPED = "stopped"

    __str__ = str.__str__


RealtimeTranscriptionEnumUpdateStatusOrStr: TypeAlias = Annotated[
    RealtimeTranscriptionEnumUpdateStatus | str, open_enum_validator(RealtimeTranscriptionEnumUpdateStatus)
]
