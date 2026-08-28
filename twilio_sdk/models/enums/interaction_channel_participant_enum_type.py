from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelParticipantEnumType(str, Enum):
    """Participant type. Can be: ``agent``, ``customer``, ``supervisor``, ``external``, ``unknown``"""

    SUPERVISOR = "supervisor"
    CUSTOMER = "customer"
    EXTERNAL = "external"
    AGENT = "agent"
    UNKNOWN = "unknown"

    __str__ = str.__str__


InteractionChannelParticipantEnumTypeOrStr: TypeAlias = Annotated[
    InteractionChannelParticipantEnumType | str, open_enum_validator(InteractionChannelParticipantEnumType)
]
