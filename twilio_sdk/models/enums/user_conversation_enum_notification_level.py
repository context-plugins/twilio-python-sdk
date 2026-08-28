from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UserConversationEnumNotificationLevel(str, Enum):
    """The Notification Level of this User Conversation. One of ``default`` or ``muted``."""

    DEFAULT = "default"
    MUTED = "muted"

    __str__ = str.__str__


UserConversationEnumNotificationLevelOrStr: TypeAlias = Annotated[
    UserConversationEnumNotificationLevel | str, open_enum_validator(UserConversationEnumNotificationLevel)
]
