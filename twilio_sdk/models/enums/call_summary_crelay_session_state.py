from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallSummaryCrelaySessionState(str, Enum):
    UNKNOWN = "unknown"
    FAILURE = "failure"
    ENDED = "ended"
    HUNG_UP = "hung_up"

    __str__ = str.__str__


CallSummaryCrelaySessionStateOrStr: TypeAlias = Annotated[
    CallSummaryCrelaySessionState | str, open_enum_validator(CallSummaryCrelaySessionState)
]
