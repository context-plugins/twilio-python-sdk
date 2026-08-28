from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_composition import VideoV1Composition, VideoV1CompositionDict


class ListCompositionResponse(SdkBaseModel):
    compositions: Optional[list[VideoV1Composition]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCompositionResponseDict(TypedDict):
    compositions: NotRequired[list[VideoV1Composition | VideoV1CompositionDict]]
    meta: NotRequired[Meta | MetaDict]
