from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .word import Word, WordDict


class Transcription(SdkBaseModel):
    """Transcription metadata."""

    channel: Optional[int] = UNSET
    """Audio channel identifier (0 for inbound, 1 for outbound)."""

    confidence: Optional[float] = UNSET
    """Overall confidence score for the transcription (0.0-1.0)."""

    engine: Optional[str] = UNSET
    """Transcription engine used."""

    words: Optional[list[Word]] = UNSET
    """Word-level transcription data with timing information."""


class TranscriptionDict(TypedDict):
    channel: NotRequired[int]
    confidence: NotRequired[float]
    engine: NotRequired[str]
    words: NotRequired[list[Word | WordDict]]
