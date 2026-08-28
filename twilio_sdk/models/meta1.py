from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta1(SdkBaseModel):
    key: str
    """The key of the list property contains the actual data items"""

    page_size: int = Field(alias="pageSize")
    """The actual number of items returned in this response"""

    previous_token: Optional[str] = Field(default=UNSET, alias="previousToken")
    """Token to fetch the previous page of results"""

    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    """Token to fetch the next page of results"""


class Meta1Dict(TypedDict):
    key: str
    page_size: int
    previous_token: NotRequired[str]
    next_token: NotRequired[str]
