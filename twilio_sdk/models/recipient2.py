from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel6 import Channel6OrStr


class Recipient2(SdkBaseModel):
    address: str
    channel: Channel6OrStr
    participant_id: Optional[str] = Field(default=UNSET, alias="participantId")


class Recipient2Dict(TypedDict):
    address: str
    channel: Channel6OrStr
    participant_id: NotRequired[str]
