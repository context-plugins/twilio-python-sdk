from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address1 import Address1, Address1Dict
from .enums.type3 import Type3OrStr


class Participant(SdkBaseModel):
    name: Optional[str] = UNSET
    """Display name for the Participant."""

    type_: Optional[Type3OrStr] = Field(default=UNSET, alias="type")
    """Type of Participant in the Conversation."""

    profile_id: Optional[str] = Field(default=UNSET, alias="profileId")
    """Resolved profile ID."""

    addresses: Optional[list[Address1]] = UNSET
    """List of Communication addresses for the Participant."""


class ParticipantDict(TypedDict):
    name: NotRequired[str]
    type_: NotRequired[Type3OrStr]
    profile_id: NotRequired[str]
    addresses: NotRequired[list[Address1 | Address1Dict]]
