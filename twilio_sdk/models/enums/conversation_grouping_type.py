from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationGroupingType(str, Enum):
    """Type of Conversation grouping strategy:
    - ``GROUP_BY_PROFILE``: Groups Communications by resolved Profile from the Memory Store.
      A Profile is looked up or created for ``CUSTOMER`` Participant types. All Communications from the same Profile are
        in the same Conversation, regardless of address or channel.
    - ``GROUP_BY_PARTICIPANT_ADDRESSES``: Groups Communications by Participant addresses across all channels.
      A customer using +18005550100 will be in the same Conversation whether they contact by SMS, WhatsApp, or RCS.
    - ``GROUP_BY_PARTICIPANT_ADDRESSES_AND_CHANNEL_TYPE``: Groups Communications by both Participant addresses AND
        channel.
      A customer using +18005550100 by SMS will be in a different Conversation than the same customer by Voice."""

    GROUP_BY_PROFILE = "GROUP_BY_PROFILE"
    GROUP_BY_PARTICIPANT_ADDRESSES = "GROUP_BY_PARTICIPANT_ADDRESSES"
    GROUP_BY_PARTICIPANT_ADDRESSES_AND_CHANNEL_TYPE = "GROUP_BY_PARTICIPANT_ADDRESSES_AND_CHANNEL_TYPE"

    __str__ = str.__str__


ConversationGroupingTypeOrStr: TypeAlias = Annotated[
    ConversationGroupingType | str, open_enum_validator(ConversationGroupingType)
]
