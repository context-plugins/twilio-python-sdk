from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessagePurpose(str, Enum):
    """Purpose of SMS messages"""

    TRANSACTIONAL = "TRANSACTIONAL"
    PROMOTIONAL = "PROMOTIONAL"

    __str__ = str.__str__


MessagePurposeOrStr: TypeAlias = Annotated[MessagePurpose | str, open_enum_validator(MessagePurpose)]
