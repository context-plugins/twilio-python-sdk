from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service_rate_limit import VerifyV2ServiceRateLimit, VerifyV2ServiceRateLimitDict


class ListRateLimitResponse(SdkBaseModel):
    rate_limits: Optional[list[VerifyV2ServiceRateLimit]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRateLimitResponseDict(TypedDict):
    rate_limits: NotRequired[list[VerifyV2ServiceRateLimit | VerifyV2ServiceRateLimitDict]]
    meta: NotRequired[Meta | MetaDict]
