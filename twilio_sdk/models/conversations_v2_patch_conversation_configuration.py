from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v2_status_callback_config import (
    ConversationsV2StatusCallbackConfig,
    ConversationsV2StatusCallbackConfigDict,
)


class ConversationsV2PatchConversationConfiguration(SdkBaseModel):
    """Partial configuration update for an existing conversation. Only statusCallbacks can be modified."""

    status_callbacks: Optional[list[ConversationsV2StatusCallbackConfig]] = Field(
        default=UNSET, alias="statusCallbacks"
    )
    """List of webhook configurations for this conversation. Send an empty array to clear all callbacks and stop webhook
    delivery."""


class ConversationsV2PatchConversationConfigurationDict(TypedDict):
    status_callbacks: NotRequired[list[ConversationsV2StatusCallbackConfig | ConversationsV2StatusCallbackConfigDict]]
