from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service_rate_limit_bucket import VerifyV2ServiceRateLimitBucket, VerifyV2ServiceRateLimitBucketDict


class ListBucketResponse(SdkBaseModel):
    buckets: Optional[list[VerifyV2ServiceRateLimitBucket]] = UNSET
    meta: Optional[Meta] = UNSET


class ListBucketResponseDict(TypedDict):
    buckets: NotRequired[list[VerifyV2ServiceRateLimitBucket | VerifyV2ServiceRateLimitBucketDict]]
    meta: NotRequired[Meta | MetaDict]
