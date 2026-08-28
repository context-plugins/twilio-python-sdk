from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .channel_settings1 import ChannelSettings1, ChannelSettings1Dict
from .enums.conversation_grouping_type3 import ConversationGroupingType3OrStr
from .status_callback1 import StatusCallback1, StatusCallback1Dict


class V2ControlPlaneConfigurationsRequest1(SdkBaseModel):
    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """A human-readable name for the configuration. Limited to 32 characters."""

    description: str
    """Human-readable description for the configuration."""

    conversation_grouping_type: ConversationGroupingType3OrStr = Field(alias="conversationGroupingType")
    """The strategy Conversation Orchestrator uses to assign communications to conversations."""

    memory_store_id: str = Field(alias="memoryStoreId")
    """The Memory Store ID for profile resolution."""

    channel_settings: dict[str, ChannelSettings1] = Field(alias="channelSettings")
    status_callbacks: Optional[list[StatusCallback1]] = Field(default=UNSET, alias="statusCallbacks")
    intelligence_configuration_ids: Optional[list[str]] = Field(default=UNSET, alias="intelligenceConfigurationIds")
    """A list of Conversational Intelligence configuration IDs."""

    memory_extraction_enabled: Optional[bool] = Field(default=UNSET, alias="memoryExtractionEnabled")
    """Whether memory extraction is enabled for conversations under this configuration. Defaults to false."""


class V2ControlPlaneConfigurationsRequest1Dict(TypedDict):
    display_name: NotRequired[str]
    description: str
    conversation_grouping_type: ConversationGroupingType3OrStr
    memory_store_id: str
    channel_settings: dict[str, ChannelSettings1 | ChannelSettings1Dict]
    status_callbacks: NotRequired[list[StatusCallback1 | StatusCallback1Dict]]
    intelligence_configuration_ids: NotRequired[list[str]]
    memory_extraction_enabled: NotRequired[bool]
