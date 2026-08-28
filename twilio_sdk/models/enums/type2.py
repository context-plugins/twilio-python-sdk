from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type2(str, Enum):
    """Type of Participant in the Conversation."""

    HUMAN_AGENT = "HUMAN_AGENT"
    CUSTOMER = "CUSTOMER"
    AI_AGENT = "AI_AGENT"
    AGENT = "AGENT"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


Type2OrStr: TypeAlias = Annotated[Type2 | str, open_enum_validator(Type2)]
