from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type21 import Type21OrStr
from .transcription import Transcription, TranscriptionDict


class ContentTranscription(SdkBaseModel):
    type_: Type21OrStr = Field(alias="type")
    """Content type discriminator."""

    text: str
    """Transcribed text."""

    transcription: Optional[Transcription] = UNSET
    """Transcription metadata."""


class ContentTranscriptionDict(TypedDict):
    type_: Type21OrStr
    text: str
    transcription: NotRequired[Transcription | TranscriptionDict]
