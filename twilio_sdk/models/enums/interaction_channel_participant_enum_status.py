from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelParticipantEnumStatus(str, Enum):
    CLOSED = "closed"
    WRAPUP = "wrapup"

    __str__ = str.__str__


InteractionChannelParticipantEnumStatusOrStr: TypeAlias = Annotated[
    InteractionChannelParticipantEnumStatus | str, open_enum_validator(InteractionChannelParticipantEnumStatus)
]
