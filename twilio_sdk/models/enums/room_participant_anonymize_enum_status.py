from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomParticipantAnonymizeEnumStatus(str, Enum):
    """The status of the Participant. Can be: ``connected`` or ``disconnected``."""

    CONNECTED = "connected"
    DISCONNECTED = "disconnected"

    __str__ = str.__str__


RoomParticipantAnonymizeEnumStatusOrStr: TypeAlias = Annotated[
    RoomParticipantAnonymizeEnumStatus | str, open_enum_validator(RoomParticipantAnonymizeEnumStatus)
]
