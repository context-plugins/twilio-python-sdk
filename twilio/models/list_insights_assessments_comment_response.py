from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_insights_assessments_comment import FlexV1InsightsAssessmentsComment, FlexV1InsightsAssessmentsCommentDict
from .meta import Meta, MetaDict


class ListInsightsAssessmentsCommentResponse(SdkBaseModel):
    comments: Optional[list[FlexV1InsightsAssessmentsComment]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInsightsAssessmentsCommentResponseDict(TypedDict):
    comments: NotRequired[list[FlexV1InsightsAssessmentsComment | FlexV1InsightsAssessmentsCommentDict]]
    meta: NotRequired[Meta | MetaDict]
