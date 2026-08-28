from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel6 import Channel6OrStr


class Address11(SdkBaseModel):
    channel: Channel6OrStr
    address: str
    channel_id: Optional[str] = Field(default=UNSET, alias="channelId")


class Address11Dict(TypedDict):
    channel: Channel6OrStr
    address: str
    channel_id: NotRequired[str]
