from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Transcription1(SdkBaseModel):
    channel: Optional[int] = UNSET
    confidence: Optional[float] = UNSET
    engine: Optional[str] = UNSET


class Transcription1Dict(TypedDict):
    channel: NotRequired[int]
    confidence: NotRequired[float]
    engine: NotRequired[str]
