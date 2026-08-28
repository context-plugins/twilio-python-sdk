from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .capabilities2 import Capabilities2, Capabilities2Dict
from .enums.dependent_order_enum_status import DependentOrderEnumStatusOrStr
from .enums.dependent_order_enum_verification_type import DependentOrderEnumVerificationTypeOrStr


class NumbersV3HostedNumbersHostedNumberOrder(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this HostedNumberOrder."""

    account_sid: OptionalNullable[str] = Field(default=UNSET, alias="accountSid")
    """A 34 character string that uniquely identifies the account."""

    incoming_phone_number_sid: OptionalNullable[str] = Field(default=UNSET, alias="incomingPhoneNumberSid")
    """A 34 character string that uniquely identifies the `IncomingPhoneNumber
    <https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource>`__ resource that represents the phone
    number being hosted."""

    address_sid: OptionalNullable[str] = Field(default=UNSET, alias="addressSid")
    """A 34 character string that uniquely identifies the Address resource that represents the address of the owner of
    this phone number."""

    signing_document_sid: OptionalNullable[str] = Field(default=UNSET, alias="signingDocumentSid")
    """A 34 character string that uniquely identifies the `Authorization Document
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource>`__ the
    user needs to sign."""

    phone_number: OptionalNullable[str] = Field(default=UNSET, alias="phoneNumber")
    """Phone number to be hosted. This must be in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format, e.g.,
    +16175551212"""

    capabilities: OptionalNullable[Capabilities2] = UNSET
    """Set of booleans describing the capabilities hosted on Twilio's platform. SMS is currently only supported."""

    friendly_name: OptionalNullable[str] = Field(default=UNSET, alias="friendlyName")
    """A 64 character string that is a human-readable text that describes this resource."""

    unique_name: OptionalNullable[str] = Field(default=UNSET, alias="uniqueName")
    """Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be
    optionally used in addition to SID."""

    status: Optional[DependentOrderEnumStatusOrStr] = UNSET
    failure_reason: OptionalNullable[str] = Field(default=UNSET, alias="failureReason")
    """A message that explains why a hosted_number_order went to status "action-required"
    """

    date_created: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="dateCreated")
    """The date this resource was created, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="dateUpdated")
    """The date that this resource was updated, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__
    format."""

    verification_attempts: Optional[int] = Field(default=UNSET, alias="verificationAttempts")
    """The number of attempts made to verify ownership of the phone number that is being hosted."""

    email: OptionalNullable[str] = UNSET
    """Email of the owner of this phone number that is being hosted."""

    cc_emails: Optional[list[str | None]] = Field(default=UNSET, alias="ccEmails")
    """A list of emails that LOA document for this HostedNumberOrder will be carbon copied to."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this HostedNumberOrder."""

    verification_type: Optional[DependentOrderEnumVerificationTypeOrStr] = Field(
        default=UNSET, alias="verificationType"
    )
    verification_document_sid: OptionalNullable[str] = Field(default=UNSET, alias="verificationDocumentSid")
    """A 34 character string that uniquely identifies the Identity Document resource that represents the document for
    verifying ownership of the number to be hosted."""

    extension: OptionalNullable[str] = UNSET
    """A numerical extension to be used when making the ownership verification call."""

    call_delay: Optional[int] = Field(default=UNSET, alias="callDelay")
    """A value between 0-30 specifying the number of seconds to delay initiating the ownership verification call."""

    verification_code: OptionalNullable[str] = Field(default=UNSET, alias="verificationCode")
    """A verification code provided in the response for a user to enter when they pick up the phone call."""

    verification_call_sids: Optional[list[str | None]] = Field(default=UNSET, alias="verificationCallSids")
    """A list of 34 character strings that are unique identifiers for the calls placed as part of ownership
    verification."""


class NumbersV3HostedNumbersHostedNumberOrderDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    incoming_phone_number_sid: NotRequired[str | None]
    address_sid: NotRequired[str | None]
    signing_document_sid: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    capabilities: NotRequired[Capabilities2 | Capabilities2Dict | None]
    friendly_name: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    status: NotRequired[DependentOrderEnumStatusOrStr]
    failure_reason: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    verification_attempts: NotRequired[int]
    email: NotRequired[str | None]
    cc_emails: NotRequired[list[str | None]]
    url: NotRequired[AnyUrl | None]
    verification_type: NotRequired[DependentOrderEnumVerificationTypeOrStr]
    verification_document_sid: NotRequired[str | None]
    extension: NotRequired[str | None]
    call_delay: NotRequired[int]
    verification_code: NotRequired[str | None]
    verification_call_sids: NotRequired[list[str | None]]
