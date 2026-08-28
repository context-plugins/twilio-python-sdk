from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageEnumAddressRetention(str, Enum):
    """Determines if the address can be stored or obfuscated based on privacy settings"""

    RETAIN = "retain"
    OBFUSCATE = "obfuscate"

    __str__ = str.__str__


MessageEnumAddressRetentionOrStr: TypeAlias = Annotated[
    MessageEnumAddressRetention | str, open_enum_validator(MessageEnumAddressRetention)
]
