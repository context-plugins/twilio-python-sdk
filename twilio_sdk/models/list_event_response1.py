from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v1_call_event import InsightsV1CallEvent, InsightsV1CallEventDict
from .meta import Meta, MetaDict


class ListEventResponse1(SdkBaseModel):
    events: Optional[list[InsightsV1CallEvent]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEventResponse1Dict(TypedDict):
    events: NotRequired[list[InsightsV1CallEvent | InsightsV1CallEventDict]]
    meta: NotRequired[Meta | MetaDict]
