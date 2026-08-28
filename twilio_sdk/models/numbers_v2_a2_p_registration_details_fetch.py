from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class NumbersV2A2PRegistrationDetailsFetch(SdkBaseModel):
    """Single A2P registration details response including brand and campaign identifiers"""

    account_sid: str = Field(alias="accountSid")
    """Account Sid that the phone number belongs to in Twilio. This is only returned for phone numbers that already
    exist in Twilio's inventory and belong to your account or sub account."""

    phone_number_sid: str = Field(alias="phoneNumberSid")
    """Phone Number SID for the requested phone number resource"""

    phone_number: str = Field(alias="phoneNumber")
    external_phone_number_status: str = Field(alias="externalPhoneNumberStatus")
    campaign_sid: OptionalNullable[str] = Field(default=UNSET, alias="campaignSid")
    """Campaign Sid associated with the phone number"""

    messaging_service_sid: OptionalNullable[str] = Field(default=UNSET, alias="messagingServiceSid")
    """Messaging Service Sid that the number is associated with"""

    external_campaign_id: OptionalNullable[str] = Field(default=UNSET, alias="externalCampaignId")
    """The identifier for a campaign in the registrar. Typically, this is the TCR Campaign Id."""

    last_updated: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdated")
    """The date and time when the A2P registration details were last updated"""

    brand_registration_sid: OptionalNullable[str] = Field(default=UNSET, alias="brandRegistrationSid")
    """Sid associated with campaign's brand"""

    external_brand_id: OptionalNullable[str] = Field(default=UNSET, alias="externalBrandId")
    """The external brand identifier (e.g., TCR Brand ID)"""


class NumbersV2A2PRegistrationDetailsFetchDict(TypedDict):
    account_sid: str
    phone_number_sid: str
    phone_number: str
    external_phone_number_status: str
    campaign_sid: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    external_campaign_id: NotRequired[str | None]
    last_updated: NotRequired[RFC3339DateTime | None]
    brand_registration_sid: NotRequired[str | None]
    external_brand_id: NotRequired[str | None]
