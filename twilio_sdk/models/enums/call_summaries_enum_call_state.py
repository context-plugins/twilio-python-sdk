from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallSummariesEnumCallState(str, Enum):
    RINGING = "ringing"
    COMPLETED = "completed"
    BUSY = "busy"
    FAIL = "fail"
    NOANSWER = "noanswer"
    CANCELED = "canceled"
    ANSWERED = "answered"
    UNDIALED = "undialed"

    __str__ = str.__str__


CallSummariesEnumCallStateOrStr: TypeAlias = Annotated[
    CallSummariesEnumCallState | str, open_enum_validator(CallSummariesEnumCallState)
]
