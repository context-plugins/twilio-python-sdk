from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v2_capture_rule import ConversationsV2CaptureRule, ConversationsV2CaptureRuleDict
from .conversations_v2_status_timeouts import ConversationsV2StatusTimeouts, ConversationsV2StatusTimeoutsDict


class ConversationsV2ChannelSetting(SdkBaseModel):
    """Configuration settings for a specific channel type."""

    status_timeouts: Optional[ConversationsV2StatusTimeouts] = Field(default=UNSET, alias="statusTimeouts")
    """Timeout settings for channel status transitions."""

    capture_rules: Optional[list[ConversationsV2CaptureRule]] = Field(default=UNSET, alias="captureRules")
    """Array of capture rules with from/to addresses and optional metadata. Use ``*`` for wildcard matching in either
    direction."""


class ConversationsV2ChannelSettingDict(TypedDict):
    status_timeouts: NotRequired[ConversationsV2StatusTimeouts | ConversationsV2StatusTimeoutsDict]
    capture_rules: NotRequired[list[ConversationsV2CaptureRule | ConversationsV2CaptureRuleDict]]
