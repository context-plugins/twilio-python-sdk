from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flows_page_component import FlowsPageComponent, FlowsPageComponentDict


class FlowsPage(SdkBaseModel):
    id: str
    next_page_id: Optional[str] = UNSET
    title: str
    subtitle: Optional[str] = UNSET
    layout: list[FlowsPageComponent]


class FlowsPageDict(TypedDict):
    id: str
    next_page_id: NotRequired[str]
    title: str
    subtitle: NotRequired[str]
    layout: list[FlowsPageComponent | FlowsPageComponentDict]
