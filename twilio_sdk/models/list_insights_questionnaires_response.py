from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_insights_questionnaires import FlexV1InsightsQuestionnaires, FlexV1InsightsQuestionnairesDict
from .meta import Meta, MetaDict


class ListInsightsQuestionnairesResponse(SdkBaseModel):
    questionnaires: Optional[list[FlexV1InsightsQuestionnaires]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInsightsQuestionnairesResponseDict(TypedDict):
    questionnaires: NotRequired[list[FlexV1InsightsQuestionnaires | FlexV1InsightsQuestionnairesDict]]
    meta: NotRequired[Meta | MetaDict]
