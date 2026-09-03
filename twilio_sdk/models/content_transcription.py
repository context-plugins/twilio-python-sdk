from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transcription import Transcription, TranscriptionDict


class ContentTranscription(SdkBaseModel):
    type_: Literal["TRANSCRIPTION"] = Field(default="TRANSCRIPTION", alias="type")
    """Content type discriminator."""

    text: str
    """Transcribed text."""

    transcription: Optional[Transcription] = UNSET
    """Transcription metadata."""


class ContentTranscriptionDict(TypedDict):
    type_: NotRequired[Literal["TRANSCRIPTION"]]
    text: str
    transcription: NotRequired[Transcription | TranscriptionDict]
