from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_recording_recording_transcription import (
    ApiV2010AccountRecordingRecordingTranscription,
    ApiV2010AccountRecordingRecordingTranscriptionDict,
)


class ListRecordingTranscriptionResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[AnyUrl] = UNSET
    next_page_uri: OptionalNullable[AnyUrl] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[AnyUrl] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[AnyUrl] = UNSET
    transcriptions: Optional[list[ApiV2010AccountRecordingRecordingTranscription]] = UNSET


class ListRecordingTranscriptionResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[AnyUrl]
    next_page_uri: NotRequired[AnyUrl | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[AnyUrl | None]
    start: NotRequired[int]
    uri: NotRequired[AnyUrl]
    transcriptions: NotRequired[
        list[ApiV2010AccountRecordingRecordingTranscription | ApiV2010AccountRecordingRecordingTranscriptionDict]
    ]
