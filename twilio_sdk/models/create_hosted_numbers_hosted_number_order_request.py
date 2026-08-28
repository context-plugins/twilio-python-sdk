from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.dependent_order_enum_verification_type import DependentOrderEnumVerificationTypeOrStr


class CreateHostedNumbersHostedNumberOrderRequest(SdkBaseModel):
    phone_number: str = Field(alias="phoneNumber")
    """The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format"""

    sms_capability: bool = Field(alias="smsCapability")
    """Used to specify that the SMS capability will be hosted on Twilio's platform."""

    account_sid: Optional[str] = Field(default=UNSET, alias="accountSid")
    """This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a
    subaccount to add the HostedNumberOrder to."""

    friendly_name: Optional[str] = Field(default=UNSET, alias="friendlyName")
    """A 64 character string that is a human readable text that describes this resource."""

    unique_name: Optional[str] = Field(default=UNSET, alias="uniqueName")
    """Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the
    developer, to be optionally used in addition to SID."""

    cc_emails: Optional[list[str]] = Field(default=UNSET, alias="ccEmails")
    """Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to."""

    sms_url: Optional[AnyUrl] = Field(default=UNSET, alias="smsUrl")
    """The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the
    IncomingPhoneNumber resource."""

    sms_method: Optional[AmdStatusCallbackMethodOrStr] = Field(default=UNSET, alias="smsMethod")
    """The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``. This will be
    copied onto the IncomingPhoneNumber resource."""

    sms_fallback_url: Optional[AnyUrl] = Field(default=UNSET, alias="smsFallbackUrl")
    """A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will
    be copied onto the IncomingPhoneNumber resource."""

    sms_fallback_method: Optional[AmdStatusCallbackMethodOrStr] = Field(default=UNSET, alias="smsFallbackMethod")
    """The HTTP method that should be used to request the SmsFallbackUrl. Must be either ``GET`` or ``POST``. This will
    be copied onto the IncomingPhoneNumber resource."""

    status_callback_url: Optional[AnyUrl] = Field(default=UNSET, alias="statusCallbackUrl")
    """Optional. The Status Callback URL attached to the IncomingPhoneNumber resource."""

    status_callback_method: Optional[AmdStatusCallbackMethodOrStr] = Field(default=UNSET, alias="statusCallbackMethod")
    """Optional. The Status Callback Method attached to the IncomingPhoneNumber resource."""

    sms_application_sid: Optional[str] = Field(default=UNSET, alias="smsApplicationSid")
    """Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number.
    If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS urls above and use those set on the
    application."""

    address_sid: Optional[str] = Field(default=UNSET, alias="addressSid")
    """Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the
    owner of this phone number."""

    email: Optional[str] = UNSET
    """Optional. Email of the owner of this phone number that is being hosted."""

    verification_type: Optional[DependentOrderEnumVerificationTypeOrStr] = Field(
        default=UNSET, alias="verificationType"
    )
    verification_document_sid: Optional[str] = Field(default=UNSET, alias="verificationDocumentSid")
    """Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership
    of the number to be hosted. Required when VerificationType is phone-bill."""


class CreateHostedNumbersHostedNumberOrderRequestDict(TypedDict):
    phone_number: str
    sms_capability: bool
    account_sid: NotRequired[str]
    friendly_name: NotRequired[str]
    unique_name: NotRequired[str]
    cc_emails: NotRequired[list[str]]
    sms_url: NotRequired[AnyUrl]
    sms_method: NotRequired[AmdStatusCallbackMethodOrStr]
    sms_fallback_url: NotRequired[AnyUrl]
    sms_fallback_method: NotRequired[AmdStatusCallbackMethodOrStr]
    status_callback_url: NotRequired[AnyUrl]
    status_callback_method: NotRequired[AmdStatusCallbackMethodOrStr]
    sms_application_sid: NotRequired[str]
    address_sid: NotRequired[str]
    email: NotRequired[str]
    verification_type: NotRequired[DependentOrderEnumVerificationTypeOrStr]
    verification_document_sid: NotRequired[str]
