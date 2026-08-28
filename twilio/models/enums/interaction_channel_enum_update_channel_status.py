from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelEnumUpdateChannelStatus(str, Enum):
    CLOSED = "closed"
    INACTIVE = "inactive"

    __str__ = str.__str__


InteractionChannelEnumUpdateChannelStatusOrStr: TypeAlias = Annotated[
    InteractionChannelEnumUpdateChannelStatus | str, open_enum_validator(InteractionChannelEnumUpdateChannelStatus)
]
