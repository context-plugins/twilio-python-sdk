from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type111 import Type111OrStr
from .transcription1 import Transcription1, Transcription1Dict


class ContentTranscription1(SdkBaseModel):
    type_: Type111OrStr = Field(alias="type")
    text: str
    transcription: Optional[Transcription1] = UNSET


class ContentTranscription1Dict(TypedDict):
    type_: Type111OrStr
    text: str
    transcription: NotRequired[Transcription1 | Transcription1Dict]
