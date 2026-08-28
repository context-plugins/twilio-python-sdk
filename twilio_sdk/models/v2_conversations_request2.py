from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v2_patch_conversation_configuration import (
    ConversationsV2PatchConversationConfiguration,
    ConversationsV2PatchConversationConfigurationDict,
)
from .enums.status7 import Status7OrStr


class V2ConversationsRequest2(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the Conversation."""

    status: Optional[Status7OrStr] = UNSET
    """The state of the Conversation."""

    configuration: Optional[ConversationsV2PatchConversationConfiguration] = UNSET
    """Partial configuration update for an existing conversation. Only statusCallbacks can be modified."""


class V2ConversationsRequest2Dict(TypedDict):
    name: NotRequired[str]
    status: NotRequired[Status7OrStr]
    configuration: NotRequired[
        ConversationsV2PatchConversationConfiguration | ConversationsV2PatchConversationConfigurationDict
    ]
