from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceUserConversationEnumNotificationLevel(str, Enum):
    """The Notification Level of this User Conversation. One of ``default`` or ``muted``."""

    DEFAULT = "default"
    MUTED = "muted"

    __str__ = str.__str__


ServiceUserConversationEnumNotificationLevelOrStr: TypeAlias = Annotated[
    ServiceUserConversationEnumNotificationLevel | str,
    open_enum_validator(ServiceUserConversationEnumNotificationLevel),
]
