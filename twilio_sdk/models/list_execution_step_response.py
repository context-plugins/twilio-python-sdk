from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .studio_v1_flow_execution_execution_step import (
    StudioV1FlowExecutionExecutionStep,
    StudioV1FlowExecutionExecutionStepDict,
)


class ListExecutionStepResponse(SdkBaseModel):
    steps: Optional[list[StudioV1FlowExecutionExecutionStep]] = UNSET
    meta: Optional[Meta] = UNSET


class ListExecutionStepResponseDict(TypedDict):
    steps: NotRequired[list[StudioV1FlowExecutionExecutionStep | StudioV1FlowExecutionExecutionStepDict]]
    meta: NotRequired[Meta | MetaDict]
