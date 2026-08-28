from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address11 import Address11, Address11Dict
from .enums.type3 import Type3OrStr


class V2ConversationsParticipantsRequest1(SdkBaseModel):
    name: Optional[str] = UNSET
    type_: Optional[Type3OrStr] = Field(default=UNSET, alias="type")
    profile_id: Optional[str] = Field(default=UNSET, alias="profileId")
    addresses: Optional[list[Address11]] = UNSET


class V2ConversationsParticipantsRequest1Dict(TypedDict):
    name: NotRequired[str]
    type_: NotRequired[Type3OrStr]
    profile_id: NotRequired[str]
    addresses: NotRequired[list[Address11 | Address11Dict]]
