from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageInteractionEnumType(str, Enum):
    """The Type of Message Interaction. This value is always ``message``."""

    MESSAGE = "message"
    VOICE = "voice"
    UNKNOWN = "unknown"

    __str__ = str.__str__


MessageInteractionEnumTypeOrStr: TypeAlias = Annotated[
    MessageInteractionEnumType | str, open_enum_validator(MessageInteractionEnumType)
]
