from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v1_call_metric import InsightsV1CallMetric, InsightsV1CallMetricDict
from .meta import Meta, MetaDict


class ListMetricResponse(SdkBaseModel):
    metrics: Optional[list[InsightsV1CallMetric]] = UNSET
    meta: Optional[Meta] = UNSET


class ListMetricResponseDict(TypedDict):
    metrics: NotRequired[list[InsightsV1CallMetric | InsightsV1CallMetricDict]]
    meta: NotRequired[Meta | MetaDict]
