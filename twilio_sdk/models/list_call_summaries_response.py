from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v1_call_summaries import InsightsV1CallSummaries, InsightsV1CallSummariesDict
from .meta import Meta, MetaDict


class ListCallSummariesResponse(SdkBaseModel):
    call_summaries: Optional[list[InsightsV1CallSummaries]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCallSummariesResponseDict(TypedDict):
    call_summaries: NotRequired[list[InsightsV1CallSummaries | InsightsV1CallSummariesDict]]
    meta: NotRequired[Meta | MetaDict]
