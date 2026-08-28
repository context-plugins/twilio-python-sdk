from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_recording import VideoV1Recording, VideoV1RecordingDict


class ListRecordingResponse1(SdkBaseModel):
    recordings: Optional[list[VideoV1Recording]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRecordingResponse1Dict(TypedDict):
    recordings: NotRequired[list[VideoV1Recording | VideoV1RecordingDict]]
    meta: NotRequired[Meta | MetaDict]
