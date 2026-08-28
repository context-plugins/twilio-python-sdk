from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v1_flow import StudioV1Flow, StudioV1FlowDict


class ListFlowResponse(SdkBaseModel):
    flows: Optional[list[StudioV1Flow]] = UNSET
    meta: Optional[Meta] = UNSET


class ListFlowResponseDict(TypedDict):
    flows: NotRequired[list[StudioV1Flow | StudioV1FlowDict]]
    meta: NotRequired[Meta | MetaDict]
