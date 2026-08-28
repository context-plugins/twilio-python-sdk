from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .video_v1_composition_hook import VideoV1CompositionHook, VideoV1CompositionHookDict


class ListCompositionHookResponse(SdkBaseModel):
    composition_hooks: Optional[list[VideoV1CompositionHook]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCompositionHookResponseDict(TypedDict):
    composition_hooks: NotRequired[list[VideoV1CompositionHook | VideoV1CompositionHookDict]]
    meta: NotRequired[Meta | MetaDict]
