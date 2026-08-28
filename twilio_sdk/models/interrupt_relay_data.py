from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .interrupt_event import InterruptEvent, InterruptEventDict


class InterruptRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""

    interrupt: InterruptEvent


class InterruptRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
    interrupt: InterruptEvent | InterruptEventDict
