from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .capabilities import Capabilities, CapabilitiesDict
from .enums.dependent_hosted_number_order_enum_status import DependentHostedNumberOrderEnumStatusOrStr


class NumbersV2AuthorizationDocumentDependentHostedNumberOrder(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this Authorization Document"""

    bulk_hosting_request_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the bulk hosting request associated with this
    HostedNumberOrder."""

    next_step: OptionalNullable[str] = UNSET
    """The next step you need to take to complete the hosted number order and request it successfully."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    incoming_phone_number_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this
    HostedNumberOrder."""

    address_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the Address resource that represents the address of the owner of
    this phone number."""

    signing_document_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder."""

    phone_number: OptionalNullable[str] = UNSET
    """An E164 formatted phone number hosted by this HostedNumberOrder."""

    capabilities: OptionalNullable[Capabilities] = UNSET
    """A mapping of capabilities this hosted phone number will have enabled on Twilio's platform."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human readable description of this resource, up to 128 characters."""

    status: Optional[DependentHostedNumberOrderEnumStatusOrStr] = UNSET
    """Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled,
    5. failed. See the section entitled `Status Values
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
    for more information on each of these statuses."""

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
    """Email recipients who will be informed when an Authorization Document has been sent and signed"""

    contact_title: OptionalNullable[str] = UNSET
    """The title of the person authorized to sign the Authorization Document for this phone number."""

    contact_phone_number: OptionalNullable[str] = UNSET
    """The contact phone number of the person authorized to sign the Authorization Document."""


class NumbersV2AuthorizationDocumentDependentHostedNumberOrderDict(TypedDict):
    sid: NotRequired[str | None]
    bulk_hosting_request_sid: NotRequired[str | None]
    next_step: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    incoming_phone_number_sid: NotRequired[str | None]
    address_sid: NotRequired[str | None]
    signing_document_sid: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    capabilities: NotRequired[Capabilities | CapabilitiesDict | None]
    friendly_name: NotRequired[str | None]
    status: NotRequired[DependentHostedNumberOrderEnumStatusOrStr]
    failure_reason: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    email: NotRequired[str | None]
    cc_emails: NotRequired[list[str | None]]
    contact_title: NotRequired[str | None]
    contact_phone_number: NotRequired[str | None]
