from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v2_flow import StudioV2Flow, StudioV2FlowDict


class ListFlowResponse1(SdkBaseModel):
    flows: Optional[list[StudioV2Flow]] = UNSET
    meta: Optional[Meta] = UNSET


class ListFlowResponse1Dict(TypedDict):
    flows: NotRequired[list[StudioV2Flow | StudioV2FlowDict]]
    meta: NotRequired[Meta | MetaDict]
