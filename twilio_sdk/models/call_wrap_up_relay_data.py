from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .call_wrap_up_event import CallWrapUpEvent, CallWrapUpEventDict


class CallWrapUpRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""

    call_wrap_up: CallWrapUpEvent


class CallWrapUpRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
    call_wrap_up: CallWrapUpEvent | CallWrapUpEventDict
