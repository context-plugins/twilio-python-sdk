from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumContentRetention(str, Enum):
    """Determines if the message content can be stored or redacted based on privacy settings"""

    RETAIN = "retain"
    DISCARD = "discard"

    __str__ = str.__str__


MessageEnumContentRetentionOrStr: TypeAlias = Annotated[
    MessageEnumContentRetention | str, open_enum_validator(MessageEnumContentRetention)
]
