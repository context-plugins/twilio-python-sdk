from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceConversationWithParticipantsEnumState(str, Enum):
    """Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or ``closed`` and
    defaults to ``active``"""

    INITIALIZING = "initializing"
    INACTIVE = "inactive"
    ACTIVE = "active"
    CLOSED = "closed"

    __str__ = str.__str__


ServiceConversationWithParticipantsEnumStateOrStr: TypeAlias = Annotated[
    ServiceConversationWithParticipantsEnumState | str,
    open_enum_validator(ServiceConversationWithParticipantsEnumState),
]
