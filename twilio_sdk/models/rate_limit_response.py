from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RateLimitResponse(SdkBaseModel):
    """Rate limit response schema"""

    field: Optional[str] = UNSET
    """Limit of requests for the bucket"""

    limit: Optional[int] = UNSET
    """Limit of requests for the bucket"""

    bucket: Optional[str] = UNSET
    """Name of the bucket"""

    owner: Optional[str] = UNSET
    """Owner of the rule"""

    ttl: Optional[int] = UNSET
    """Time to live of the rule"""


class RateLimitResponseDict(TypedDict):
    field: NotRequired[str]
    limit: NotRequired[int]
    bucket: NotRequired[str]
    owner: NotRequired[str]
    ttl: NotRequired[int]
