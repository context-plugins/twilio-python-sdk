from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_insights_questionnaires_category import (
    FlexV1InsightsQuestionnairesCategory,
    FlexV1InsightsQuestionnairesCategoryDict,
)
from .meta import Meta, MetaDict


class ListInsightsQuestionnairesCategoryResponse(SdkBaseModel):
    categories: Optional[list[FlexV1InsightsQuestionnairesCategory]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInsightsQuestionnairesCategoryResponseDict(TypedDict):
    categories: NotRequired[list[FlexV1InsightsQuestionnairesCategory | FlexV1InsightsQuestionnairesCategoryDict]]
    meta: NotRequired[Meta | MetaDict]
