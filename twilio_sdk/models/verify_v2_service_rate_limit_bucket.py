from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class VerifyV2ServiceRateLimitBucket(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this Bucket."""

    rate_limit_sid: OptionalNullable[str] = UNSET
    """The Twilio-provided string that uniquely identifies the Rate Limit resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is associated with."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Rate Limit resource."""

    max: Optional[int] = UNSET
    """Maximum number of requests permitted in during the interval."""

    interval: Optional[int] = UNSET
    """Number of seconds that the rate limit will be enforced over."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""


class VerifyV2ServiceRateLimitBucketDict(TypedDict):
    sid: NotRequired[str | None]
    rate_limit_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    max: NotRequired[int]
    interval: NotRequired[int]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
