from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationWithParticipantsEnumState(str, Enum):
    """Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or ``closed`` and
    defaults to ``active``"""

    INITIALIZING = "initializing"
    INACTIVE = "inactive"
    ACTIVE = "active"
    CLOSED = "closed"

    __str__ = str.__str__


ConversationWithParticipantsEnumStateOrStr: TypeAlias = Annotated[
    ConversationWithParticipantsEnumState | str, open_enum_validator(ConversationWithParticipantsEnumState)
]
