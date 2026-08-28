from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Flags(SdkBaseModel):
    """The flags that describe the phone number features."""

    national: Optional[bool] = Field(default=UNSET, alias="National")
    international: Optional[bool] = Field(default=UNSET, alias="International")


class FlagsDict(TypedDict):
    national: NotRequired[bool]
    international: NotRequired[bool]
