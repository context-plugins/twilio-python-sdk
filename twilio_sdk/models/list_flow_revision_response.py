from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v2_flow_flow_revision import StudioV2FlowFlowRevision, StudioV2FlowFlowRevisionDict


class ListFlowRevisionResponse(SdkBaseModel):
    revisions: Optional[list[StudioV2FlowFlowRevision]] = UNSET
    meta: Optional[Meta] = UNSET


class ListFlowRevisionResponseDict(TypedDict):
    revisions: NotRequired[list[StudioV2FlowFlowRevision | StudioV2FlowFlowRevisionDict]]
    meta: NotRequired[Meta | MetaDict]
