from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallSummariesEnumProcessingStateRequest(str, Enum):
    COMPLETED = "completed"
    STARTED = "started"
    PARTIAL = "partial"
    ALL = "all"

    __str__ = str.__str__


CallSummariesEnumProcessingStateRequestOrStr: TypeAlias = Annotated[
    CallSummariesEnumProcessingStateRequest | str, open_enum_validator(CallSummariesEnumProcessingStateRequest)
]
