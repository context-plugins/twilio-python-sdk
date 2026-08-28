from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_insights_assessments import FlexV1InsightsAssessments, FlexV1InsightsAssessmentsDict
from .meta import Meta, MetaDict


class ListInsightsAssessmentsResponse(SdkBaseModel):
    assessments: Optional[list[FlexV1InsightsAssessments]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInsightsAssessmentsResponseDict(TypedDict):
    assessments: NotRequired[list[FlexV1InsightsAssessments | FlexV1InsightsAssessmentsDict]]
    meta: NotRequired[Meta | MetaDict]
