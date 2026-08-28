from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v1_conference import InsightsV1Conference, InsightsV1ConferenceDict
from .meta import Meta, MetaDict


class ListConferenceResponse1(SdkBaseModel):
    conferences: Optional[list[InsightsV1Conference]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConferenceResponse1Dict(TypedDict):
    conferences: NotRequired[list[InsightsV1Conference | InsightsV1ConferenceDict]]
    meta: NotRequired[Meta | MetaDict]
