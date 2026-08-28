from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelInviteEnumType(str, Enum):
    TASKROUTER = "taskrouter"

    __str__ = str.__str__


InteractionChannelInviteEnumTypeOrStr: TypeAlias = Annotated[
    InteractionChannelInviteEnumType | str, open_enum_validator(InteractionChannelInviteEnumType)
]
