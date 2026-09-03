from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v2_conversations_v1_bridge import (
    ConversationsV2ConversationsV1Bridge,
    ConversationsV2ConversationsV1BridgeDict,
)
from .conversations_v2_status_callback_config import (
    ConversationsV2StatusCallbackConfig,
    ConversationsV2StatusCallbackConfigDict,
)
from .enums.conversation_grouping_type import ConversationGroupingTypeOrStr


class Configuration(SdkBaseModel):
    """Full configuration settings for this Conversation."""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """A human-readable name for the configuration. Limited to 32 characters."""

    description: Optional[str] = UNSET
    """Human-readable description for the Configuration."""

    conversation_grouping_type: Optional[ConversationGroupingTypeOrStr] = Field(
        default=UNSET, alias="conversationGroupingType"
    )
    """Type of Conversation grouping strategy:
    - ``GROUP_BY_PROFILE``: Groups Communications by resolved Profile from the Memory Store.
      A Profile is looked up or created for ``CUSTOMER`` Participant types. All Communications from the same Profile are
        in the same Conversation, regardless of address or channel.
    - ``GROUP_BY_PARTICIPANT_ADDRESSES``: Groups Communications by Participant addresses across all channels.
      A customer using +18005550100 will be in the same Conversation whether they contact by SMS, WhatsApp, or RCS.
    - ``GROUP_BY_PARTICIPANT_ADDRESSES_AND_CHANNEL_TYPE``: Groups Communications by both Participant addresses AND
        channel.
      A customer using +18005550100 by SMS will be in a different Conversation than the same customer by Voice."""

    memory_store_id: Optional[str] = Field(default=UNSET, alias="memoryStoreId")
    """Memory Store ID for Profile resolution."""

    channel_settings: Optional[Any] = Field(default=UNSET, alias="channelSettings")
    """Channel-specific parameters forwarded as-is to the downstream sending service. Allows passing backend-specific
    fields without requiring API changes."""

    status_callbacks: Optional[list[ConversationsV2StatusCallbackConfig]] = Field(
        default=UNSET, alias="statusCallbacks"
    )
    """List of default webhook configurations applied to Conversations under this Configuration."""

    intelligence_configuration_ids: Optional[list[str]] = Field(default=UNSET, alias="intelligenceConfigurationIds")
    """List of Intelligence Configuration IDs configured for this Configuration."""

    memory_extraction_enabled: Optional[bool] = Field(default=UNSET, alias="memoryExtractionEnabled")
    """Whether memory extraction is enabled for conversations under this configuration. Defaults to false."""

    conversations_v1_bridge: Optional[ConversationsV2ConversationsV1Bridge] = Field(
        default=UNSET, alias="conversationsV1Bridge"
    )
    """Configuration for Conversations V1 bridge. When set, messaging channels route through Conversations V1. Use this
    to integrate with existing Conversations V1 applications."""


class ConfigurationDict(TypedDict):
    display_name: NotRequired[str]
    description: NotRequired[str]
    conversation_grouping_type: NotRequired[ConversationGroupingTypeOrStr]
    memory_store_id: NotRequired[str]
    channel_settings: NotRequired[Any]
    status_callbacks: NotRequired[list[ConversationsV2StatusCallbackConfig | ConversationsV2StatusCallbackConfigDict]]
    intelligence_configuration_ids: NotRequired[list[str]]
    memory_extraction_enabled: NotRequired[bool]
    conversations_v1_bridge: NotRequired[
        ConversationsV2ConversationsV1Bridge | ConversationsV2ConversationsV1BridgeDict
    ]
