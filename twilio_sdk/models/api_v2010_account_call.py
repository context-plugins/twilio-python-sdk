from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.call_enum_status import CallEnumStatusOrStr


class ApiV2010AccountCall(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify this Call resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in UTC that this resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in UTC that this resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    parent_call_sid: OptionalNullable[str] = UNSET
    """The SID that identifies the call that created this leg."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this Call resource."""

    to: OptionalNullable[str] = UNSET
    """The phone number, SIP address, Client identifier or SIM SID that received this call. Phone numbers are in `E.164
    <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212). SIP addresses are formatted as
    ``name@company.com``. Client identifiers are formatted ``client:name``. SIM SIDs are formatted as ``sim:sid``."""

    to_formatted: OptionalNullable[str] = UNSET
    """The phone number, SIP address or Client identifier that received this call. Formatted for display. Non-North
    American phone numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g.,
    +442071838750)."""

    from_: OptionalNullable[str] = Field(default=UNSET, alias="from")
    """The phone number, SIP address, Client identifier or SIM SID that made this call. Phone numbers are in `E.164
    <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212). SIP addresses are formatted as
    ``name@company.com``. Client identifiers are formatted ``client:name``. SIM SIDs are formatted as ``sim:sid``."""

    from_formatted: OptionalNullable[str] = UNSET
    """The calling phone number, SIP address, or Client identifier formatted for display. Non-North American phone
    numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +442071838750)."""

    phone_number_sid: OptionalNullable[str] = UNSET
    """If the call was inbound, this is the SID of the IncomingPhoneNumber resource that received the call. If the call
    was outbound, it is the SID of the OutgoingCallerId resource from which the call was placed."""

    status: Optional[CallEnumStatusOrStr] = UNSET
    """The status of this call. Can be: ``queued``, ``ringing``, ``in-progress``, ``canceled``, ``completed``,
    ``failed``, ``busy`` or ``no-answer``. See `Call Status Values
    <https://www.twilio.com/docs/voice/api/call-resource#call-status-values>`__ below for more information."""

    start_time: OptionalNullable[str] = UNSET
    """The start time of the call, given as UTC in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format. Empty if the call has not
    yet been dialed."""

    end_time: OptionalNullable[str] = UNSET
    """The time the call ended, given as UTC in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format. Empty if the call did not
    complete successfully."""

    duration: OptionalNullable[str] = UNSET
    """The length of the call in seconds. This value is empty for busy, failed, unanswered, or ongoing calls."""

    price: OptionalNullable[str] = UNSET
    """The charge for this call, in the currency associated with the account. Populated after the call is completed. May
    not be immediately available. The price associated with a call only reflects the charge for connectivity. Charges
    for other call-related features such as Answering Machine Detection, Text-To-Speech, and SIP REFER are not included
    in this value."""

    price_unit: OptionalNullable[str] = UNSET
    """The currency in which ``Price`` is measured, in `ISO 4127
    <https://www.iso.org/iso/home/standards/currency_codes.htm>`__ format (e.g., ``USD``, ``EUR``, ``JPY``). Always
    capitalized for calls."""

    direction: OptionalNullable[str] = UNSET
    """A string describing the direction of the call. Can be: ``inbound`` for inbound calls, ``outbound-api`` for calls
    initiated via the REST API or ``outbound-dial`` for calls initiated by a ``<Dial>`` verb. Using `Elastic SIP
    Trunking <https://www.twilio.com/docs/sip-trunking>`__, the values can be
    https://www.twilio.com/docs/sip-trunking#termination for outgoing calls from your communications infrastructure to
    the PSTN or https://www.twilio.com/docs/sip-trunking#origination for incoming calls to your communications
    infrastructure from the PSTN."""

    answered_by: OptionalNullable[str] = UNSET
    """Either ``human`` or ``machine`` if this call was initiated with answering machine detection. Empty otherwise."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to create the call."""

    forwarded_from: OptionalNullable[str] = UNSET
    """The forwarding phone number if this call was an incoming call forwarded from another number (depends on carrier
    supporting forwarding). Otherwise, empty."""

    group_sid: OptionalNullable[str] = UNSET
    """The Group SID associated with this call. If no Group is associated with the call, the field is empty."""

    caller_name: OptionalNullable[str] = UNSET
    """The caller's name if this call was an incoming call to a phone number with caller ID Lookup enabled. Otherwise,
    empty."""

    queue_time: OptionalNullable[str] = UNSET
    """The wait time in milliseconds before the call is placed."""

    trunk_sid: OptionalNullable[str] = UNSET
    """The unique identifier of the trunk resource that was used for this call. The field is empty if the call was not
    made using a SIP trunk or if the call is not terminated."""

    uri: OptionalNullable[str] = UNSET
    """The URI of this resource, relative to ``https://api.twilio.com``."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of subresources available to this call, identified by their URIs relative to
    ``https://api.twilio.com``."""


class ApiV2010AccountCallDict(TypedDict):
    sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    parent_call_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    to: NotRequired[str | None]
    to_formatted: NotRequired[str | None]
    from_: NotRequired[str | None]
    from_formatted: NotRequired[str | None]
    phone_number_sid: NotRequired[str | None]
    status: NotRequired[CallEnumStatusOrStr]
    start_time: NotRequired[str | None]
    end_time: NotRequired[str | None]
    duration: NotRequired[str | None]
    price: NotRequired[str | None]
    price_unit: NotRequired[str | None]
    direction: NotRequired[str | None]
    answered_by: NotRequired[str | None]
    api_version: NotRequired[str | None]
    forwarded_from: NotRequired[str | None]
    group_sid: NotRequired[str | None]
    caller_name: NotRequired[str | None]
    queue_time: NotRequired[str | None]
    trunk_sid: NotRequired[str | None]
    uri: NotRequired[str | None]
    subresource_uris: NotRequired[Any | None]
