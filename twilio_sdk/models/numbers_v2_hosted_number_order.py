from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .capabilities import Capabilities, CapabilitiesDict
from .enums.dependent_order_enum_status import DependentOrderEnumStatusOrStr
from .enums.hosted_number_order_enum_verification_type1 import HostedNumberOrderEnumVerificationType1OrStr


class NumbersV2HostedNumberOrder(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this HostedNumberOrder."""

    account_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the account."""

    incoming_phone_number_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the `IncomingPhoneNumber
    <https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource>`__ resource that represents the phone
    number being hosted."""

    address_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the Address resource that represents the address of the owner of
    this phone number."""

    signing_document_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the `Authorization Document
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource>`__ the
    user needs to sign."""

    phone_number: OptionalNullable[str] = UNSET
    """Phone number to be hosted. This must be in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format, e.g.,
    +16175551212"""

    capabilities: OptionalNullable[Capabilities] = UNSET
    """Set of booleans describing the capabilities hosted on Twilio's platform. SMS is currently only supported."""

    friendly_name: OptionalNullable[str] = UNSET
    """A 128 character string that is a human-readable text that describes this resource."""

    status: Optional[DependentOrderEnumStatusOrStr] = UNSET
    """Status of this resource. It can hold one of the values: 1. Twilio Processing 2. Received, 3. Pending LOA, 4.
    Carrier Processing, 5. Completed, 6. Action Required, 7. Failed. See the `HostedNumberOrders Status Values
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values>`__
    section for more information on each of these statuses."""

    failure_reason: OptionalNullable[str] = UNSET
    """A message that explains why a hosted_number_order went to status "action-required"
    """

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date this resource was created, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was updated, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__
    format."""

    email: OptionalNullable[str] = UNSET
    """Email of the owner of this phone number that is being hosted."""

    cc_emails: Optional[list[str | None]] = UNSET
    """A list of emails that LOA document for this HostedNumberOrder will be carbon copied to."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this HostedNumberOrder."""

    contact_title: OptionalNullable[str] = UNSET
    """The title of the person authorized to sign the Authorization Document for this phone number."""

    contact_phone_number: OptionalNullable[str] = UNSET
    """The contact phone number of the person authorized to sign the Authorization Document."""

    bulk_hosting_request_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the bulk hosting request associated with this
    HostedNumberOrder."""

    next_step: OptionalNullable[str] = UNSET
    """The next step you need to take to complete the hosted number order and request it successfully."""

    verification_attempts: Optional[int] = UNSET
    """The number of attempts made to verify ownership via a call for the hosted phone number."""

    verification_call_sids: Optional[list[str | None]] = UNSET
    """The Call SIDs that identify the calls placed to verify ownership."""

    verification_call_delay: Optional[int] = UNSET
    """The number of seconds to wait before initiating the ownership verification call. Can be a value between 0 and 60,
    inclusive."""

    verification_call_extension: OptionalNullable[str] = UNSET
    """The numerical extension to dial when making the ownership verification call."""

    verification_code: OptionalNullable[str] = UNSET
    """The digits the user must pass in the ownership verification call."""

    verification_type: Optional[HostedNumberOrderEnumVerificationType1OrStr] = UNSET
    """The method used to verify ownership of the number to be hosted. Can be: ``phone-call`` or ``phone-bill`` and the
    default is ``phone-call``."""


class NumbersV2HostedNumberOrderDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    incoming_phone_number_sid: NotRequired[str | None]
    address_sid: NotRequired[str | None]
    signing_document_sid: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    capabilities: NotRequired[Capabilities | CapabilitiesDict | None]
    friendly_name: NotRequired[str | None]
    status: NotRequired[DependentOrderEnumStatusOrStr]
    failure_reason: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    email: NotRequired[str | None]
    cc_emails: NotRequired[list[str | None]]
    url: NotRequired[AnyUrl | None]
    contact_title: NotRequired[str | None]
    contact_phone_number: NotRequired[str | None]
    bulk_hosting_request_sid: NotRequired[str | None]
    next_step: NotRequired[str | None]
    verification_attempts: NotRequired[int]
    verification_call_sids: NotRequired[list[str | None]]
    verification_call_delay: NotRequired[int]
    verification_call_extension: NotRequired[str | None]
    verification_code: NotRequired[str | None]
    verification_type: NotRequired[HostedNumberOrderEnumVerificationType1OrStr]
