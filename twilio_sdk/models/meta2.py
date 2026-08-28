from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta2(SdkBaseModel):
    key: Optional[str] = UNSET
    page_size: Optional[int] = Field(default=UNSET, alias="pageSize")
    previous_token: Optional[str] = Field(default=UNSET, alias="previousToken")
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")


class Meta2Dict(TypedDict):
    key: NotRequired[str]
    page_size: NotRequired[int]
    previous_token: NotRequired[str]
    next_token: NotRequired[str]
