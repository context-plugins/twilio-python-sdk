from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FlowsPageComponent(SdkBaseModel):
    label: Optional[str] = UNSET
    type_: str = Field(alias="type")


class FlowsPageComponentDict(TypedDict):
    label: NotRequired[str]
    type_: str
