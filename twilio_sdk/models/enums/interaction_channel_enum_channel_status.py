from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelEnumChannelStatus(str, Enum):
    """The status of this channel."""

    SETUP = "setup"
    ACTIVE = "active"
    FAILED = "failed"
    CLOSED = "closed"
    INACTIVE = "inactive"
    PAUSE = "pause"
    TRANSFER = "transfer"

    __str__ = str.__str__


InteractionChannelEnumChannelStatusOrStr: TypeAlias = Annotated[
    InteractionChannelEnumChannelStatus | str, open_enum_validator(InteractionChannelEnumChannelStatus)
]
