from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .conversations_v2_channel_setting import ConversationsV2ChannelSetting, ConversationsV2ChannelSettingDict
from .conversations_v2_conversations_v1_bridge import (
    ConversationsV2ConversationsV1Bridge,
    ConversationsV2ConversationsV1BridgeDict,
)
from .conversations_v2_status_callback_config import (
    ConversationsV2StatusCallbackConfig,
    ConversationsV2StatusCallbackConfigDict,
)
from .enums.conversation_grouping_type import ConversationGroupingTypeOrStr


class ConversationsV2Configuration(SdkBaseModel):
    """Configuration for Conversations."""

    id: str
    """Configuration ID."""

    display_name: str = Field(alias="displayName")
    """A human-readable name for the configuration. Limited to 32 characters."""

    description: str
    """Human-readable description for the Configuration. Allows spaces and special characters, typically limited to a
    paragraph of text. This serves as a descriptive field rather than just a name."""

    conversation_grouping_type: ConversationGroupingTypeOrStr = Field(alias="conversationGroupingType")
    """Type of Conversation grouping strategy:
    - ``GROUP_BY_PROFILE``: Groups Communications by resolved Profile from the Memory Store.
      A Profile is looked up or created for ``CUSTOMER`` Participant types. All Communications from the same Profile are
        in the same Conversation, regardless of address or channel.
    - ``GROUP_BY_PARTICIPANT_ADDRESSES``: Groups Communications by Participant addresses across all channels.
      A customer using +18005550100 will be in the same Conversation whether they contact by SMS, WhatsApp, or RCS.
    - ``GROUP_BY_PARTICIPANT_ADDRESSES_AND_CHANNEL_TYPE``: Groups Communications by both Participant addresses AND
        channel.
      A customer using +18005550100 by SMS will be in a different Conversation than the same customer by Voice."""

    memory_store_id: str = Field(alias="memoryStoreId")
    """Memory Store ID for Profile resolution."""

    channel_settings: Optional[dict[str, ConversationsV2ChannelSetting]] = Field(default=UNSET, alias="channelSettings")
    """Channel-specific configuration settings by channel type. Keys should be valid channel types (``VOICE``, ``SMS``,
    ``RCS``, ``WHATSAPP``, ``CHAT``)."""

    status_callbacks: Optional[list[ConversationsV2StatusCallbackConfig]] = Field(
        default=UNSET, alias="statusCallbacks"
    )
    """List of default webhook configurations applied to Conversations under this Configuration."""

    intelligence_configuration_ids: Optional[list[str]] = Field(default=UNSET, alias="intelligenceConfigurationIds")
    """A list of Conversational Intelligence configuration IDs."""

    memory_extraction_enabled: Optional[bool] = Field(default=UNSET, alias="memoryExtractionEnabled")
    """Whether memory extraction is enabled for conversations under this configuration. Defaults to false."""

    conversations_v1_bridge: Optional[ConversationsV2ConversationsV1Bridge] = Field(
        default=UNSET, alias="conversationsV1Bridge"
    )
    """Configuration for Conversations V1 bridge. When set, messaging channels route through Conversations V1. Use this
    to integrate with existing Conversations V1 applications."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Timestamp when this Configuration was created."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Timestamp when this Configuration was last updated."""

    version: Optional[int] = UNSET
    """Version number used for optimistic locking."""


class ConversationsV2ConfigurationDict(TypedDict):
    id: str
    display_name: str
    description: str
    conversation_grouping_type: ConversationGroupingTypeOrStr
    memory_store_id: str
    channel_settings: NotRequired[dict[str, ConversationsV2ChannelSetting | ConversationsV2ChannelSettingDict]]
    status_callbacks: NotRequired[list[ConversationsV2StatusCallbackConfig | ConversationsV2StatusCallbackConfigDict]]
    intelligence_configuration_ids: NotRequired[list[str]]
    memory_extraction_enabled: NotRequired[bool]
    conversations_v1_bridge: NotRequired[
        ConversationsV2ConversationsV1Bridge | ConversationsV2ConversationsV1BridgeDict
    ]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    version: NotRequired[int]
