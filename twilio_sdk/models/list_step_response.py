from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v1_flow_engagement_step import StudioV1FlowEngagementStep, StudioV1FlowEngagementStepDict


class ListStepResponse(SdkBaseModel):
    steps: Optional[list[StudioV1FlowEngagementStep]] = UNSET
    meta: Optional[Meta] = UNSET


class ListStepResponseDict(TypedDict):
    steps: NotRequired[list[StudioV1FlowEngagementStep | StudioV1FlowEngagementStepDict]]
    meta: NotRequired[Meta | MetaDict]
