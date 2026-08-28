from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_event import ErrorEvent, ErrorEventDict


class ErrorRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""

    error: ErrorEvent


class ErrorRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
    error: ErrorEvent | ErrorEventDict
