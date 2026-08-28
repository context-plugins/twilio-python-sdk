from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr


class ConversationsV2StatusCallbackConfig(SdkBaseModel):
    """Default webhook configuration for Conversation-level events under this Configuration."""

    url: AnyUrl
    """Destination URL for webhooks."""

    method: Optional[AmdStatusCallbackMethodOrStr] = UNSET
    """HTTP method used to invoke the webhook URL."""


class ConversationsV2StatusCallbackConfigDict(TypedDict):
    url: AnyUrl
    method: NotRequired[AmdStatusCallbackMethodOrStr]
