from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.bundle_enum_status import BundleEnumStatusOrStr


class NumbersV2RegulatoryComplianceBundle(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Bundle resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Bundle resource."""

    regulation_sid: OptionalNullable[str] = UNSET
    """The unique string of a regulation that is associated to the Bundle resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    status: Optional[BundleEnumStatusOrStr] = UNSET
    """The verification status of the Bundle resource."""

    valid_until: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format when the resource will
    be valid until."""

    email: OptionalNullable[str] = UNSET
    """The email address that will receive updates when the Bundle resource changes status."""

    status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL we call to inform your application of status changes."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Bundle resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of the Assigned Items of the Bundle resource."""


class NumbersV2RegulatoryComplianceBundleDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    regulation_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    status: NotRequired[BundleEnumStatusOrStr]
    valid_until: NotRequired[RFC3339DateTime | None]
    email: NotRequired[str | None]
    status_callback: NotRequired[AnyUrl | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
