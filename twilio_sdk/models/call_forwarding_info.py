from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallForwardingInfo(SdkBaseModel):
    call_forwarding_enabled: Optional[bool] = UNSET
    error_code: Optional[int] = UNSET


class CallForwardingInfoDict(TypedDict):
    call_forwarding_enabled: NotRequired[bool]
    error_code: NotRequired[int]
