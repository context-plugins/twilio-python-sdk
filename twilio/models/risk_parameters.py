from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RiskParameters(SdkBaseModel):
    partner_sub_id: Optional[str] = UNSET


class RiskParametersDict(TypedDict):
    partner_sub_id: NotRequired[str]
