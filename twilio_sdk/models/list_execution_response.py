from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v1_flow_execution import StudioV1FlowExecution, StudioV1FlowExecutionDict


class ListExecutionResponse(SdkBaseModel):
    executions: Optional[list[StudioV1FlowExecution]] = UNSET
    meta: Optional[Meta] = UNSET


class ListExecutionResponseDict(TypedDict):
    executions: NotRequired[list[StudioV1FlowExecution | StudioV1FlowExecutionDict]]
    meta: NotRequired[Meta | MetaDict]
