from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.brand_vetting_enum_vetting_provider import BrandVettingEnumVettingProviderOrStr


class MessagingV1BrandRegistrationsBrandVetting(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the vetting record."""

    brand_sid: OptionalNullable[str] = UNSET
    """The unique string to identify Brand Registration."""

    brand_vetting_sid: OptionalNullable[str] = UNSET
    """The Twilio SID of the third-party vetting record."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    vetting_id: OptionalNullable[str] = UNSET
    """The unique identifier of the vetting from the third-party provider."""

    vetting_class: OptionalNullable[str] = UNSET
    """The type of vetting that has been conducted. One of “STANDARD” (Aegis) or “POLITICAL” (Campaign Verify)."""

    vetting_status: OptionalNullable[str] = UNSET
    """The status of the import vetting attempt. One of “PENDING,” “SUCCESS,” or “FAILED”."""

    vetting_provider: Optional[BrandVettingEnumVettingProviderOrStr] = UNSET
    """The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign Verify tokens) or
    “AEGIS” (Secondary Vetting)."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Brand Vetting resource."""


class MessagingV1BrandRegistrationsBrandVettingDict(TypedDict):
    account_sid: NotRequired[str | None]
    brand_sid: NotRequired[str | None]
    brand_vetting_sid: NotRequired[str | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    date_created: NotRequired[RFC3339DateTime | None]
    vetting_id: NotRequired[str | None]
    vetting_class: NotRequired[str | None]
    vetting_status: NotRequired[str | None]
    vetting_provider: NotRequired[BrandVettingEnumVettingProviderOrStr]
    url: NotRequired[str | None]
