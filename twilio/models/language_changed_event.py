from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LanguageChangedEvent(SdkBaseModel):
    tts_language_code: Optional[str] = UNSET
    transcription_language_code: Optional[str] = UNSET


class LanguageChangedEventDict(TypedDict):
    tts_language_code: NotRequired[str]
    transcription_language_code: NotRequired[str]
