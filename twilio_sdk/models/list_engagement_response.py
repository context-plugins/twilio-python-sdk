from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v1_flow_engagement import StudioV1FlowEngagement, StudioV1FlowEngagementDict


class ListEngagementResponse(SdkBaseModel):
    engagements: Optional[list[StudioV1FlowEngagement]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEngagementResponseDict(TypedDict):
    engagements: NotRequired[list[StudioV1FlowEngagement | StudioV1FlowEngagementDict]]
    meta: NotRequired[Meta | MetaDict]
