from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationGroupingType3(str, Enum):
    """The strategy Conversation Orchestrator uses to assign communications to conversations."""

    GROUP_BY_PROFILE = "GROUP_BY_PROFILE"
    GROUP_BY_PARTICIPANT_ADDRESSES = "GROUP_BY_PARTICIPANT_ADDRESSES"
    GROUP_BY_PARTICIPANT_ADDRESSES_AND_CHANNEL_TYPE = "GROUP_BY_PARTICIPANT_ADDRESSES_AND_CHANNEL_TYPE"

    __str__ = str.__str__


ConversationGroupingType3OrStr: TypeAlias = Annotated[
    ConversationGroupingType3 | str, open_enum_validator(ConversationGroupingType3)
]
