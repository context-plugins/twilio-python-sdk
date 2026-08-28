from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallEnumStatus(str, Enum):
    """The status of this call. Can be: ``queued``, ``ringing``, ``in-progress``, ``canceled``, ``completed``,
    ``failed``, ``busy`` or ``no-answer``. See `Call Status Values
    <https://www.twilio.com/docs/voice/api/call-resource#call-status-values>`__ below for more information."""

    QUEUED = "queued"
    RINGING = "ringing"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    BUSY = "busy"
    FAILED = "failed"
    NO_ANSWER = "no-answer"
    CANCELED = "canceled"

    __str__ = str.__str__


CallEnumStatusOrStr: TypeAlias = Annotated[CallEnumStatus | str, open_enum_validator(CallEnumStatus)]
