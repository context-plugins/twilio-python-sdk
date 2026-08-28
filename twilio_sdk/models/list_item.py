from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListItem(SdkBaseModel):
    id: str
    item: str
    description: Optional[str] = UNSET


class ListItemDict(TypedDict):
    id: str
    item: str
    description: NotRequired[str]
