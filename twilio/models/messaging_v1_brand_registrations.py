from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.brand_registrations_enum_brand_feedback import BrandRegistrationsEnumBrandFeedbackOrStr
from .enums.brand_registrations_enum_identity_status import BrandRegistrationsEnumIdentityStatusOrStr
from .enums.brand_registrations_enum_status import BrandRegistrationsEnumStatusOrStr


class MessagingV1BrandRegistrations(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string to identify Brand Registration."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Brand Registration
    resource."""

    customer_profile_bundle_sid: OptionalNullable[str] = UNSET
    """A2P Messaging Profile Bundle BundleSid."""

    a2p_profile_bundle_sid: OptionalNullable[str] = UNSET
    """A2P Messaging Profile Bundle BundleSid."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    brand_type: OptionalNullable[str] = UNSET
    """Type of brand. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for the low volume, SOLE_PROPRIETOR
    campaign use case. There can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR brand. STANDARD is for
    all other campaign use cases. Multiple campaign use cases can be created per STANDARD brand."""

    status: Optional[BrandRegistrationsEnumStatusOrStr] = UNSET
    """Brand Registration status. One of "PENDING", "APPROVED", "FAILED", "IN_REVIEW", "DELETION_PENDING",
    "DELETION_FAILED", "SUSPENDED"."""

    tcr_id: OptionalNullable[str] = UNSET
    """Campaign Registry (TCR) Brand ID. Assigned only after successful brand registration."""

    failure_reason: OptionalNullable[str] = UNSET
    """DEPRECATED. A reason why brand registration has failed. Only applicable when status is FAILED."""

    errors: Optional[list[Any | None]] = UNSET
    """A list of errors that occurred during the brand registration process."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Brand Registration resource."""

    brand_score: OptionalNullable[int] = UNSET
    """The secondary vetting score if it was done. Otherwise, it will be the brand score if it's returned from TCR. It
    may be null if no score is available."""

    brand_feedback: Optional[list[BrandRegistrationsEnumBrandFeedbackOrStr | None]] = UNSET
    """DEPRECATED. Feedback on how to improve brand score"""

    identity_status: Optional[BrandRegistrationsEnumIdentityStatusOrStr] = UNSET
    """When a brand is registered, TCR will attempt to verify the identity of the brand based on the supplied
    information."""

    russell_3000: OptionalNullable[bool] = UNSET
    """Publicly traded company identified in the Russell 3000 Index"""

    government_entity: OptionalNullable[bool] = UNSET
    """Identified as a government entity"""

    tax_exempt_status: OptionalNullable[str] = UNSET
    """Nonprofit organization tax-exempt status per section 501 of the U.S. tax code."""

    skip_automatic_sec_vet: OptionalNullable[bool] = UNSET
    """A flag to disable automatic secondary vetting for brands which it would otherwise be done."""

    mock: OptionalNullable[bool] = UNSET
    """A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock
    brand. Defaults to false if no value is provided."""

    links: OptionalNullable[Any] = UNSET


class MessagingV1BrandRegistrationsDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    customer_profile_bundle_sid: NotRequired[str | None]
    a2p_profile_bundle_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    brand_type: NotRequired[str | None]
    status: NotRequired[BrandRegistrationsEnumStatusOrStr]
    tcr_id: NotRequired[str | None]
    failure_reason: NotRequired[str | None]
    errors: NotRequired[list[Any | None]]
    url: NotRequired[str | None]
    brand_score: NotRequired[int | None]
    brand_feedback: NotRequired[list[BrandRegistrationsEnumBrandFeedbackOrStr | None]]
    identity_status: NotRequired[BrandRegistrationsEnumIdentityStatusOrStr]
    russell_3000: NotRequired[bool | None]
    government_entity: NotRequired[bool | None]
    tax_exempt_status: NotRequired[str | None]
    skip_automatic_sec_vet: NotRequired[bool | None]
    mock: NotRequired[bool | None]
    links: NotRequired[Any | None]
