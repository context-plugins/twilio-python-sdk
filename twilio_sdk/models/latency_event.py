from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LatencyEvent(SdkBaseModel):
    latency_ms: Optional[int] = UNSET
    """Latency in milliseconds."""


class LatencyEventDict(TypedDict):
    latency_ms: NotRequired[int]
