from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_insights_questionnaires_question import (
    FlexV1InsightsQuestionnairesQuestion,
    FlexV1InsightsQuestionnairesQuestionDict,
)
from .meta import Meta, MetaDict


class ListInsightsQuestionnairesQuestionResponse(SdkBaseModel):
    questions: Optional[list[FlexV1InsightsQuestionnairesQuestion]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInsightsQuestionnairesQuestionResponseDict(TypedDict):
    questions: NotRequired[list[FlexV1InsightsQuestionnairesQuestion | FlexV1InsightsQuestionnairesQuestionDict]]
    meta: NotRequired[Meta | MetaDict]
