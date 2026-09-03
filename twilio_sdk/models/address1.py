from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel5 import Channel5OrStr


class Address1(SdkBaseModel):
    channel: Channel5OrStr
    address: str
    channel_id: Optional[str] = Field(default=UNSET, alias="channelId")


class Address1Dict(TypedDict):
    channel: Channel5OrStr
    address: str
    channel_id: NotRequired[str]
