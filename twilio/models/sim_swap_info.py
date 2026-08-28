from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .last_sim_swap_info import LastSimSwapInfo, LastSimSwapInfoDict


class SimSwapInfo(SdkBaseModel):
    last_sim_swap: Optional[LastSimSwapInfo] = UNSET
    carrier_name: Optional[str] = UNSET
    mobile_country_code: Optional[str] = UNSET
    mobile_network_code: Optional[str] = UNSET
    error_code: Optional[int] = UNSET


class SimSwapInfoDict(TypedDict):
    last_sim_swap: NotRequired[LastSimSwapInfo | LastSimSwapInfoDict]
    carrier_name: NotRequired[str]
    mobile_country_code: NotRequired[str]
    mobile_network_code: NotRequired[str]
    error_code: NotRequired[int]
