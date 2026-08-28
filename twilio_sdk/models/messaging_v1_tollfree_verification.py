from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.tollfree_verification_enum_business_registration_authority import (
    TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr,
)
from .enums.tollfree_verification_enum_business_type import TollfreeVerificationEnumBusinessTypeOrStr
from .enums.tollfree_verification_enum_opt_in_type import TollfreeVerificationEnumOptInTypeOrStr
from .enums.tollfree_verification_enum_status import TollfreeVerificationEnumStatusOrStr
from .enums.tollfree_verification_enum_use_case_category import TollfreeVerificationEnumUseCaseCategoryOrStr
from .enums.tollfree_verification_enum_vetting_provider import TollfreeVerificationEnumVettingProviderOrStr


class MessagingV1TollfreeVerification(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string to identify Tollfree Verification."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Tollfree Verification
    resource."""

    customer_profile_sid: OptionalNullable[str] = UNSET
    """Customer's Profile Bundle BundleSid."""

    trust_product_sid: OptionalNullable[str] = UNSET
    """Tollfree TrustProduct Bundle BundleSid."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    regulated_item_sid: OptionalNullable[str] = UNSET
    """The SID of the Regulated Item."""

    business_name: OptionalNullable[str] = UNSET
    """The name of the business or organization using the Tollfree number."""

    business_street_address: OptionalNullable[str] = UNSET
    """The address of the business or organization using the Tollfree number."""

    business_street_address2: OptionalNullable[str] = UNSET
    """The address of the business or organization using the Tollfree number."""

    business_city: OptionalNullable[str] = UNSET
    """The city of the business or organization using the Tollfree number."""

    business_state_province_region: OptionalNullable[str] = UNSET
    """The state/province/region of the business or organization using the Tollfree number."""

    business_postal_code: OptionalNullable[str] = UNSET
    """The postal code of the business or organization using the Tollfree number."""

    business_country: OptionalNullable[str] = UNSET
    """The country of the business or organization using the Tollfree number."""

    business_website: OptionalNullable[str] = UNSET
    """The website of the business or organization using the Tollfree number."""

    business_contact_first_name: OptionalNullable[str] = UNSET
    """The first name of the contact for the business or organization using the Tollfree number."""

    business_contact_last_name: OptionalNullable[str] = UNSET
    """The last name of the contact for the business or organization using the Tollfree number."""

    business_contact_email: OptionalNullable[str] = UNSET
    """The email address of the contact for the business or organization using the Tollfree number."""

    business_contact_phone: OptionalNullable[str] = UNSET
    """The E.164 formatted phone number of the contact for the business or organization using the Tollfree number."""

    notification_email: OptionalNullable[str] = UNSET
    """The email address to receive the notification about the verification result. ."""

    use_case_categories: Optional[list[TollfreeVerificationEnumUseCaseCategoryOrStr | None]] = UNSET
    """The category of the use case for the Tollfree Number. List as many as are applicable."""

    use_case_summary: OptionalNullable[str] = UNSET
    """Use this to further explain how messaging is used by the business or organization."""

    production_message_sample: OptionalNullable[str] = UNSET
    """An example of message content, i.e. a sample message."""

    opt_in_image_urls: Optional[list[str | None]] = UNSET
    """Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL."""

    opt_in_type: Optional[TollfreeVerificationEnumOptInTypeOrStr] = UNSET
    """Describe how a user opts-in to text messages."""

    message_volume: OptionalNullable[str] = UNSET
    """Estimate monthly volume of messages from the Tollfree Number."""

    additional_information: OptionalNullable[str] = UNSET
    """Additional information to be provided for verification."""

    tollfree_phone_number_sid: OptionalNullable[str] = UNSET
    """The SID of the Phone Number associated with the Tollfree Verification."""

    tollfree_phone_number: OptionalNullable[str] = UNSET
    """The E.164 formatted toll-free phone number associated with the verification."""

    status: Optional[TollfreeVerificationEnumStatusOrStr] = UNSET
    """The compliance status of the Tollfree Verification record."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Tollfree Verification resource."""

    rejection_reason: OptionalNullable[str] = UNSET
    """The rejection reason given when a Tollfree Verification has been rejected."""

    error_code: OptionalNullable[int] = UNSET
    """The error code given when a Tollfree Verification has been rejected."""

    edit_expiration: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time when the ability to edit a rejected verification expires."""

    edit_allowed: OptionalNullable[bool] = UNSET
    """If a rejected verification is allowed to be edited/resubmitted. Some rejection reasons allow editing and some do
    not."""

    business_registration_number: OptionalNullable[str] = UNSET
    """A legally recognized business registration number"""

    business_registration_authority: OptionalNullable[
        TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr
    ] = UNSET
    """The organizational authority for business registrations. Required for all business types except
    SOLE_PROPRIETOR."""

    business_registration_country: OptionalNullable[str] = UNSET
    """Country business is registered in"""

    business_type: OptionalNullable[TollfreeVerificationEnumBusinessTypeOrStr] = UNSET
    """The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, SOLE_PROPRIETOR, GOVERNMENT.
    Required field."""

    business_registration_phone_number: OptionalNullable[str] = UNSET
    """The E.164 formatted number associated with the business."""

    doing_business_as: OptionalNullable[str] = UNSET
    """Trade name, sub entity, or downstream business name of business being submitted for verification"""

    opt_in_confirmation_message: OptionalNullable[str] = UNSET
    """The confirmation message sent to users when they opt in to receive messages."""

    help_message_sample: OptionalNullable[str] = UNSET
    """A sample help message provided to users."""

    privacy_policy_url: OptionalNullable[AnyUrl] = UNSET
    """The URL to the privacy policy for the business or organization."""

    terms_and_conditions_url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the terms and conditions for the business or organization."""

    age_gated_content: OptionalNullable[bool] = UNSET
    """Indicates if the content is age gated."""

    opt_in_keywords: Optional[list[str | None]] = UNSET
    """List of keywords that users can send to opt in or out of messages."""

    rejection_reasons: Optional[list[Any | None]] = UNSET
    """A list of rejection reasons and codes describing why a Tollfree Verification has been rejected."""

    resource_links: OptionalNullable[Any] = UNSET
    """The URLs of the documents associated with the Tollfree Verification resource."""

    external_reference_id: OptionalNullable[str] = UNSET
    """An optional external reference ID supplied by customer and echoed back on status retrieval."""

    vetting_id: OptionalNullable[str] = UNSET
    vetting_provider: OptionalNullable[TollfreeVerificationEnumVettingProviderOrStr] = UNSET
    """The third-party political vetting provider."""

    vetting_id_expiration: OptionalNullable[RFC3339DateTime] = UNSET


class MessagingV1TollfreeVerificationDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    customer_profile_sid: NotRequired[str | None]
    trust_product_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    regulated_item_sid: NotRequired[str | None]
    business_name: NotRequired[str | None]
    business_street_address: NotRequired[str | None]
    business_street_address2: NotRequired[str | None]
    business_city: NotRequired[str | None]
    business_state_province_region: NotRequired[str | None]
    business_postal_code: NotRequired[str | None]
    business_country: NotRequired[str | None]
    business_website: NotRequired[str | None]
    business_contact_first_name: NotRequired[str | None]
    business_contact_last_name: NotRequired[str | None]
    business_contact_email: NotRequired[str | None]
    business_contact_phone: NotRequired[str | None]
    notification_email: NotRequired[str | None]
    use_case_categories: NotRequired[list[TollfreeVerificationEnumUseCaseCategoryOrStr | None]]
    use_case_summary: NotRequired[str | None]
    production_message_sample: NotRequired[str | None]
    opt_in_image_urls: NotRequired[list[str | None]]
    opt_in_type: NotRequired[TollfreeVerificationEnumOptInTypeOrStr]
    message_volume: NotRequired[str | None]
    additional_information: NotRequired[str | None]
    tollfree_phone_number_sid: NotRequired[str | None]
    tollfree_phone_number: NotRequired[str | None]
    status: NotRequired[TollfreeVerificationEnumStatusOrStr]
    url: NotRequired[AnyUrl | None]
    rejection_reason: NotRequired[str | None]
    error_code: NotRequired[int | None]
    edit_expiration: NotRequired[RFC3339DateTime | None]
    edit_allowed: NotRequired[bool | None]
    business_registration_number: NotRequired[str | None]
    business_registration_authority: NotRequired[TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None]
    business_registration_country: NotRequired[str | None]
    business_type: NotRequired[TollfreeVerificationEnumBusinessTypeOrStr | None]
    business_registration_phone_number: NotRequired[str | None]
    doing_business_as: NotRequired[str | None]
    opt_in_confirmation_message: NotRequired[str | None]
    help_message_sample: NotRequired[str | None]
    privacy_policy_url: NotRequired[AnyUrl | None]
    terms_and_conditions_url: NotRequired[AnyUrl | None]
    age_gated_content: NotRequired[bool | None]
    opt_in_keywords: NotRequired[list[str | None]]
    rejection_reasons: NotRequired[list[Any | None]]
    resource_links: NotRequired[Any | None]
    external_reference_id: NotRequired[str | None]
    vetting_id: NotRequired[str | None]
    vetting_provider: NotRequired[TollfreeVerificationEnumVettingProviderOrStr | None]
    vetting_id_expiration: NotRequired[RFC3339DateTime | None]
