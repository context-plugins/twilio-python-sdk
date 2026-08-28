from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelEnumStatus(str, Enum):
    """The status of this channel."""

    CLOSED = "closed"
    WRAPUP = "wrapup"

    __str__ = str.__str__


InteractionChannelEnumStatusOrStr: TypeAlias = Annotated[
    InteractionChannelEnumStatus | str, open_enum_validator(InteractionChannelEnumStatus)
]
