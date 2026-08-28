from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .channel_settings import ChannelSettings, ChannelSettingsDict
from .enums.conversation_grouping_type3 import ConversationGroupingType3OrStr
from .status_callback import StatusCallback, StatusCallbackDict


class V2ControlPlaneConfigurationsRequest(SdkBaseModel):
    display_name: str = Field(alias="displayName")
    """A human-readable name for the configuration. Limited to 32 characters."""

    description: str
    """Human-readable description for the configuration."""

    conversation_grouping_type: ConversationGroupingType3OrStr = Field(alias="conversationGroupingType")
    """The strategy Conversation Orchestrator uses to assign communications to conversations."""

    memory_store_id: str = Field(alias="memoryStoreId")
    """The memory store ID that Conversation Orchestrator uses for profile resolution."""

    channel_settings: Optional[dict[str, ChannelSettings]] = Field(default=UNSET, alias="channelSettings")
    status_callbacks: Optional[list[StatusCallback]] = Field(default=UNSET, alias="statusCallbacks")
    """A list of webhook configurations."""

    intelligence_configuration_ids: Optional[list[str]] = Field(default=UNSET, alias="intelligenceConfigurationIds")
    """A list of Conversational Intelligence configuration IDs."""

    memory_extraction_enabled: Optional[bool] = Field(default=UNSET, alias="memoryExtractionEnabled")
    """Whether memory extraction is enabled for conversations under this configuration. Defaults to false."""


class V2ControlPlaneConfigurationsRequestDict(TypedDict):
    display_name: str
    description: str
    conversation_grouping_type: ConversationGroupingType3OrStr
    memory_store_id: str
    channel_settings: NotRequired[dict[str, ChannelSettings | ChannelSettingsDict]]
    status_callbacks: NotRequired[list[StatusCallback | StatusCallbackDict]]
    intelligence_configuration_ids: NotRequired[list[str]]
    memory_extraction_enabled: NotRequired[bool]
