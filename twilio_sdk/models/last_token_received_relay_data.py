from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .last_token_received_event import LastTokenReceivedEvent, LastTokenReceivedEventDict


class LastTokenReceivedRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""

    last_token_received: LastTokenReceivedEvent


class LastTokenReceivedRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
    last_token_received: LastTokenReceivedEvent | LastTokenReceivedEventDict
