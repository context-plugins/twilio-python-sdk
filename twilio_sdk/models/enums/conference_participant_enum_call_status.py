from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConferenceParticipantEnumCallStatus(str, Enum):
    ANSWERED = "answered"
    COMPLETED = "completed"
    BUSY = "busy"
    FAIL = "fail"
    NOANSWER = "noanswer"
    RINGING = "ringing"
    CANCELED = "canceled"

    __str__ = str.__str__


ConferenceParticipantEnumCallStatusOrStr: TypeAlias = Annotated[
    ConferenceParticipantEnumCallStatus | str, open_enum_validator(ConferenceParticipantEnumCallStatus)
]
