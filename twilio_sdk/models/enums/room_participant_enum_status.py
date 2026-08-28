from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoomParticipantEnumStatus(str, Enum):
    """The status of the Participant. Can be: ``connected`` or ``disconnected``."""

    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    RECONNECTING = "reconnecting"

    __str__ = str.__str__


RoomParticipantEnumStatusOrStr: TypeAlias = Annotated[
    RoomParticipantEnumStatus | str, open_enum_validator(RoomParticipantEnumStatus)
]
