from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReassignedNumberParameters(SdkBaseModel):
    last_verified_date: Optional[str] = UNSET


class ReassignedNumberParametersDict(TypedDict):
    last_verified_date: NotRequired[str]
