from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capture_rule import CaptureRule, CaptureRuleDict
from .status_timeouts import StatusTimeouts, StatusTimeoutsDict


class ChannelSettings(SdkBaseModel):
    status_timeouts: Optional[StatusTimeouts] = Field(default=UNSET, alias="statusTimeouts")
    capture_rules: Optional[list[CaptureRule]] = Field(default=UNSET, alias="captureRules")


class ChannelSettingsDict(TypedDict):
    status_timeouts: NotRequired[StatusTimeouts | StatusTimeoutsDict]
    capture_rules: NotRequired[list[CaptureRule | CaptureRuleDict]]
