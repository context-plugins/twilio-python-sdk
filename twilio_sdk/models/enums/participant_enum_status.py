from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ParticipantEnumStatus(str, Enum):
    """The status of the participant's call in a session. Can be: ``queued``, ``connecting``, ``ringing``,
    ``connected``, ``complete``, or ``failed``."""

    QUEUED = "queued"
    CONNECTING = "connecting"
    RINGING = "ringing"
    CONNECTED = "connected"
    COMPLETE = "complete"
    FAILED = "failed"

    __str__ = str.__str__


ParticipantEnumStatusOrStr: TypeAlias = Annotated[
    ParticipantEnumStatus | str, open_enum_validator(ParticipantEnumStatus)
]
