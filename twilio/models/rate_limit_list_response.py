from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .rate_limit_response import RateLimitResponse, RateLimitResponseDict


class RateLimitListResponse(SdkBaseModel):
    rate_limits: Optional[list[RateLimitResponse]] = UNSET


class RateLimitListResponseDict(TypedDict):
    rate_limits: NotRequired[list[RateLimitResponse | RateLimitResponseDict]]
