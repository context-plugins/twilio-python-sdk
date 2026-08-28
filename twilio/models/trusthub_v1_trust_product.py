from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.trust_product_enum_status import TrustProductEnumStatusOrStr


class TrusthubV1TrustProduct(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Trust Product resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Trust Product
    resource."""

    policy_sid: OptionalNullable[str] = UNSET
    """The unique string of the policy that is associated with the Trust Product resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    status: Optional[TrustProductEnumStatusOrStr] = UNSET
    """The verification status of the Trust Product resource."""

    valid_until: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format until which the resource
    will be valid."""

    email: OptionalNullable[str] = UNSET
    """The email address that will receive updates when the Trust Product resource changes status."""

    status_callback: OptionalNullable[str] = UNSET
    """The URL we call to inform your application of status changes."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Trust Product resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of the Assigned Items of the Trust Product resource."""

    errors: Optional[list[Any | None]] = UNSET
    """The error codes associated with the rejection of the Trust Product."""


class TrusthubV1TrustProductDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    policy_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    status: NotRequired[TrustProductEnumStatusOrStr]
    valid_until: NotRequired[RFC3339DateTime | None]
    email: NotRequired[str | None]
    status_callback: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
    errors: NotRequired[list[Any | None]]
