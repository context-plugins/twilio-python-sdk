from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.customer_profile_enum_status import CustomerProfileEnumStatusOrStr


class TrusthubV1CustomerProfile(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Customer-Profile resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Customer-Profile
    resource."""

    policy_sid: OptionalNullable[str] = UNSET
    """The unique string of a policy that is associated to the Customer-Profile resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    status: Optional[CustomerProfileEnumStatusOrStr] = UNSET
    """The verification status of the Customer-Profile resource."""

    valid_until: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format when the resource will
    be valid until."""

    email: OptionalNullable[str] = UNSET
    """The email address that will receive updates when the Customer-Profile resource changes status."""

    status_callback: OptionalNullable[str] = UNSET
    """The URL we call to inform your application of status changes."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Customer-Profile resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of the Assigned Items of the Customer-Profile resource."""

    errors: Optional[list[Any | None]] = UNSET
    """The error codes associated with the rejection of the Customer-Profile."""


class TrusthubV1CustomerProfileDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    policy_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    status: NotRequired[CustomerProfileEnumStatusOrStr]
    valid_until: NotRequired[RFC3339DateTime | None]
    email: NotRequired[str | None]
    status_callback: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
    errors: NotRequired[list[Any | None]]
