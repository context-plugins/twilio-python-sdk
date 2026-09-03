from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_insights_segments import FlexV1InsightsSegments, FlexV1InsightsSegmentsDict
from .meta import Meta, MetaDict


class ListInsightsSegmentsResponse(SdkBaseModel):
    segments: Optional[list[FlexV1InsightsSegments]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInsightsSegmentsResponseDict(TypedDict):
    segments: NotRequired[list[FlexV1InsightsSegments | FlexV1InsightsSegmentsDict]]
    meta: NotRequired[Meta | MetaDict]
