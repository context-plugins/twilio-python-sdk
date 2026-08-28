from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .latency_event import LatencyEvent, LatencyEventDict


class SttLatencyRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""

    stt_latency: LatencyEvent


class SttLatencyRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
    stt_latency: LatencyEvent | LatencyEventDict
