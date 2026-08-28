from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capture_rule1 import CaptureRule1, CaptureRule1Dict
from .status_timeouts1 import StatusTimeouts1, StatusTimeouts1Dict


class ChannelSettings1(SdkBaseModel):
    status_timeouts: Optional[StatusTimeouts1] = Field(default=UNSET, alias="statusTimeouts")
    capture_rules: Optional[list[CaptureRule1]] = Field(default=UNSET, alias="captureRules")


class ChannelSettings1Dict(TypedDict):
    status_timeouts: NotRequired[StatusTimeouts1 | StatusTimeouts1Dict]
    capture_rules: NotRequired[list[CaptureRule1 | CaptureRule1Dict]]
