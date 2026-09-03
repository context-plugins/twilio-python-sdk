from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelInviteEnumAction(str, Enum):
    ACCEPT = "accept"
    DECLINE = "decline"

    __str__ = str.__str__


InteractionChannelInviteEnumActionOrStr: TypeAlias = Annotated[
    InteractionChannelInviteEnumAction | str, open_enum_validator(InteractionChannelInviteEnumAction)
]
