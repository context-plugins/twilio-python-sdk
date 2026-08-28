from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .language_changed_event import LanguageChangedEvent, LanguageChangedEventDict


class LanguageChangedRelayData(SdkBaseModel):
    session_id: str
    """Session id of the conversation relay."""

    sequence_number: int
    """Sequence number of the event."""

    language_changed: LanguageChangedEvent


class LanguageChangedRelayDataDict(TypedDict):
    session_id: str
    sequence_number: int
    language_changed: LanguageChangedEvent | LanguageChangedEventDict
