from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RelyingParty(SdkBaseModel):
    """Contains the information of the party requesting the user for authentication"""

    id: Optional[str] = UNSET
    name: Optional[str] = UNSET
    origins: Optional[list[str]] = UNSET


class RelyingPartyDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    origins: NotRequired[list[str]]
