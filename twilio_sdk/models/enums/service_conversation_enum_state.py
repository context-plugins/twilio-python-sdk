from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceConversationEnumState(str, Enum):
    """Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or ``closed`` and
    defaults to ``active``"""

    INACTIVE = "inactive"
    ACTIVE = "active"
    CLOSED = "closed"
    INITIALIZING = "initializing"

    __str__ = str.__str__


ServiceConversationEnumStateOrStr: TypeAlias = Annotated[
    ServiceConversationEnumState | str, open_enum_validator(ServiceConversationEnumState)
]
