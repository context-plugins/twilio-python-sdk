from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transcription1 import Transcription1, Transcription1Dict


class ContentTranscription1(SdkBaseModel):
    type_: Literal["TRANSCRIPTION"] = Field(default="TRANSCRIPTION", alias="type")
    text: str
    transcription: Optional[Transcription1] = UNSET


class ContentTranscription1Dict(TypedDict):
    type_: NotRequired[Literal["TRANSCRIPTION"]]
    text: str
    transcription: NotRequired[Transcription1 | Transcription1Dict]
