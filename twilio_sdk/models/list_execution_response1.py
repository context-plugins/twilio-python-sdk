from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v2_flow_execution import StudioV2FlowExecution, StudioV2FlowExecutionDict


class ListExecutionResponse1(SdkBaseModel):
    executions: Optional[list[StudioV2FlowExecution]] = UNSET
    meta: Optional[Meta] = UNSET


class ListExecutionResponse1Dict(TypedDict):
    executions: NotRequired[list[StudioV2FlowExecution | StudioV2FlowExecutionDict]]
    meta: NotRequired[Meta | MetaDict]
