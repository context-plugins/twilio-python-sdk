from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BaseRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""


class BaseRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
