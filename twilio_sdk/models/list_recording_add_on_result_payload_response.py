from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload import (
    ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload,
    ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayloadDict,
)


class ListRecordingAddOnResultPayloadResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[AnyUrl] = UNSET
    next_page_uri: OptionalNullable[AnyUrl] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[AnyUrl] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[AnyUrl] = UNSET
    payloads: Optional[list[ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload]] = UNSET


class ListRecordingAddOnResultPayloadResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[AnyUrl]
    next_page_uri: NotRequired[AnyUrl | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[AnyUrl | None]
    start: NotRequired[int]
    uri: NotRequired[AnyUrl]
    payloads: NotRequired[
        list[
            (
                ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload
                | ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayloadDict
            )
        ]
    ]
