from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class LastSimSwapInfo(SdkBaseModel):
    last_sim_swap_date: Optional[RFC3339DateTime] = UNSET
    swapped_period: Optional[str] = UNSET
    swapped_in_period: Optional[bool] = UNSET


class LastSimSwapInfoDict(TypedDict):
    last_sim_swap_date: NotRequired[RFC3339DateTime]
    swapped_period: NotRequired[str]
    swapped_in_period: NotRequired[bool]
