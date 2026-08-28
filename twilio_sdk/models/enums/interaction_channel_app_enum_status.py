from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelAppEnumStatus(str, Enum):
    ADDING = "adding"
    ACTIVE = "active"
    PAUSING = "pausing"
    PAUSED = "paused"
    RESUMING = "resuming"
    REMOVING = "removing"
    REMOVED = "removed"
    ERRORED = "errored"

    __str__ = str.__str__


InteractionChannelAppEnumStatusOrStr: TypeAlias = Annotated[
    InteractionChannelAppEnumStatus | str, open_enum_validator(InteractionChannelAppEnumStatus)
]
