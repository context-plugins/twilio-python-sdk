from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_flex_flow import FlexV1FlexFlow, FlexV1FlexFlowDict
from .meta import Meta, MetaDict


class ListFlexFlowResponse(SdkBaseModel):
    flex_flows: Optional[list[FlexV1FlexFlow]] = UNSET
    meta: Optional[Meta] = UNSET


class ListFlexFlowResponseDict(TypedDict):
    flex_flows: NotRequired[list[FlexV1FlexFlow | FlexV1FlexFlowDict]]
    meta: NotRequired[Meta | MetaDict]
