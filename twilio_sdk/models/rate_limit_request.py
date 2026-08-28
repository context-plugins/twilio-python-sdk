from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RateLimitRequest(SdkBaseModel):
    """Rate limit request schema"""

    limit: Optional[int] = UNSET
    """Limit of requests for the bucket"""

    ttl: Optional[int] = UNSET
    """Time to live of the rule"""


class RateLimitRequestDict(TypedDict):
    limit: NotRequired[int]
    ttl: NotRequired[int]
