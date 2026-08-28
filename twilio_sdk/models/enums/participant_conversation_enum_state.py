from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ParticipantConversationEnumState(str, Enum):
    """The current state of this User Conversation. One of ``inactive``, ``active`` or ``closed``."""

    INACTIVE = "inactive"
    ACTIVE = "active"
    CLOSED = "closed"

    __str__ = str.__str__


ParticipantConversationEnumStateOrStr: TypeAlias = Annotated[
    ParticipantConversationEnumState | str, open_enum_validator(ParticipantConversationEnumState)
]
