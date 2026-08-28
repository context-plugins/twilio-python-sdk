from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class VerifyV2ServiceRateLimit(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this Rate Limit."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is associated with."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Rate Limit resource."""

    unique_name: OptionalNullable[str] = UNSET
    """Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be
    optionally used in addition to SID. **This value should not contain PII.**"""

    description: OptionalNullable[str] = UNSET
    """Description of this Rate Limit"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The URL of this resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class VerifyV2ServiceRateLimitDict(TypedDict):
    sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    description: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
