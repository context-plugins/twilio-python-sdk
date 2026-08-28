from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1ServiceUsAppToPerson(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies a US A2P Compliance resource ``QE2c6890da8086d771620e9b13fadeba0b``."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that the Campaign belongs to."""

    brand_registration_sid: OptionalNullable[str] = UNSET
    """The unique string to identify the A2P brand."""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/api/service-resource>`__ that the
    resource is associated with."""

    description: OptionalNullable[str] = UNSET
    """A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters."""

    message_samples: Optional[list[str | None]] = UNSET
    """An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for
    each sample: 1024 chars."""

    us_app_to_person_usecase: OptionalNullable[str] = UNSET
    """A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING, SOLE_PROPRIETOR...]. SOLE_PROPRIETOR campaign use
    cases can only be created by SOLE_PROPRIETOR Brands, and there can only be one SOLE_PROPRIETOR campaign created per
    SOLE_PROPRIETOR Brand."""

    has_embedded_links: OptionalNullable[bool] = UNSET
    """Indicate that this SMS campaign will send messages that contain links."""

    has_embedded_phone: OptionalNullable[bool] = UNSET
    """Indicates that this SMS campaign will send messages that contain phone numbers."""

    subscriber_opt_in: OptionalNullable[bool] = UNSET
    """A boolean that specifies whether campaign has Subscriber Optin or not."""

    age_gated: OptionalNullable[bool] = UNSET
    """A boolean that specifies whether campaign is age gated or not."""

    direct_lending: OptionalNullable[bool] = UNSET
    """A boolean that specifies whether campaign allows direct lending or not."""

    campaign_status: OptionalNullable[str] = UNSET
    """Campaign status. Examples: IN_PROGRESS, VERIFIED, FAILED."""

    campaign_id: OptionalNullable[str] = UNSET
    """The Campaign Registry (TCR) Campaign ID."""

    is_externally_registered: OptionalNullable[bool] = UNSET
    """Indicates whether the campaign was registered externally or not."""

    rate_limits: OptionalNullable[Any] = UNSET
    """Rate limit and/or classification set by each carrier, Ex. AT&T or T-Mobile."""

    message_flow: OptionalNullable[str] = UNSET
    """Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If
    multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048
    character maximum."""

    opt_in_message: OptionalNullable[str] = UNSET
    """If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent
    to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in
    enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is
    required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum.
    320 character maximum."""

    opt_out_message: OptionalNullable[str] = UNSET
    """Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an
    auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further
    messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is
    required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20
    character minimum. 320 character maximum."""

    help_message: OptionalNullable[str] = UNSET
    """When customers receive the help keywords from their end users, Twilio customers are expected to send back an
    auto-generated response; this may include the brand name and additional support contact information. This field is
    required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20
    character minimum. 320 character maximum."""

    opt_in_keywords: Optional[list[str | None]] = UNSET
    """If end users can text in a keyword to start receiving messages from this campaign, those keywords must be
    provided. This field is required if end users can text in a keyword to start receiving messages from this campaign.
    Values must be alphanumeric. 255 character maximum."""

    opt_out_keywords: Optional[list[str | None]] = UNSET
    """End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must
    be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or
    Advanced Opt Out features). Values must be alphanumeric. 255 character maximum."""

    help_keywords: Optional[list[str | None]] = UNSET
    """End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the
    campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's
    Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the US App to Person resource."""

    mock: OptionalNullable[bool] = UNSET
    """A boolean that specifies whether campaign is a mock or not. Mock campaigns will be automatically created if using
    a mock brand. Mock campaigns should only be used for testing purposes."""

    errors: Optional[list[Any | None]] = UNSET
    """Details indicating why a campaign registration failed. These errors can indicate one or more fields that were
    incorrect or did not meet review requirements."""


class MessagingV1ServiceUsAppToPersonDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    brand_registration_sid: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    description: NotRequired[str | None]
    message_samples: NotRequired[list[str | None]]
    us_app_to_person_usecase: NotRequired[str | None]
    has_embedded_links: NotRequired[bool | None]
    has_embedded_phone: NotRequired[bool | None]
    subscriber_opt_in: NotRequired[bool | None]
    age_gated: NotRequired[bool | None]
    direct_lending: NotRequired[bool | None]
    campaign_status: NotRequired[str | None]
    campaign_id: NotRequired[str | None]
    is_externally_registered: NotRequired[bool | None]
    rate_limits: NotRequired[Any | None]
    message_flow: NotRequired[str | None]
    opt_in_message: NotRequired[str | None]
    opt_out_message: NotRequired[str | None]
    help_message: NotRequired[str | None]
    opt_in_keywords: NotRequired[list[str | None]]
    opt_out_keywords: NotRequired[list[str | None]]
    help_keywords: NotRequired[list[str | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    mock: NotRequired[bool | None]
    errors: NotRequired[list[Any | None]]
