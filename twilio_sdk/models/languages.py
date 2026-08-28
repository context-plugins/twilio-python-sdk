from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Languages(SdkBaseModel):
    tts_provider: Optional[str] = UNSET
    voice: Optional[str] = UNSET
    transcription_provider: Optional[str] = UNSET
    speech_model: Optional[str] = UNSET


class LanguagesDict(TypedDict):
    tts_provider: NotRequired[str]
    voice: NotRequired[str]
    transcription_provider: NotRequired[str]
    speech_model: NotRequired[str]
