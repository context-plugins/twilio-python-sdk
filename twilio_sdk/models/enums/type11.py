from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type11(str, Enum):
    """Type of Participant in the Conversation."""

    HUMAN_AGENT = "HUMAN_AGENT"
    CUSTOMER = "CUSTOMER"
    AI_AGENT = "AI_AGENT"

    __str__ = str.__str__


Type11OrStr: TypeAlias = Annotated[Type11 | str, open_enum_validator(Type11)]
