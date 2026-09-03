from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceUserConversationEnumState(str, Enum):
    """The current state of this User Conversation. One of ``inactive``, ``active`` or ``closed``."""

    INACTIVE = "inactive"
    ACTIVE = "active"
    CLOSED = "closed"

    __str__ = str.__str__


ServiceUserConversationEnumStateOrStr: TypeAlias = Annotated[
    ServiceUserConversationEnumState | str, open_enum_validator(ServiceUserConversationEnumState)
]
