from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.message_enum_direction import MessageEnumDirectionOrStr
from .enums.message_enum_status import MessageEnumStatusOrStr


class ApiV2010AccountMessage(SdkBaseModel):
    body: OptionalNullable[str] = UNSET
    """The text content of the message"""

    num_segments: OptionalNullable[str] = UNSET
    """The number of segments that make up the complete message. SMS message bodies that exceed the `character limit
    <https://www.twilio.com/docs/glossary/what-sms-character-limit>`__ are segmented and charged as multiple messages.
    Note: For messages sent via a Messaging Service, ``num_segments`` is initially ``0``, since a sender hasn't yet been
    assigned."""

    direction: Optional[MessageEnumDirectionOrStr] = UNSET
    """The direction of the message. Can be: ``inbound`` for incoming messages, ``outbound-api`` for messages created by
    the REST API, ``outbound-call`` for messages created during a call, or ``outbound-reply`` for messages created in
    response to an incoming message."""

    from_: OptionalNullable[str] = Field(default=UNSET, alias="from")
    """The sender's phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format), `alphanumeric sender ID
    <https://www.twilio.com/docs/sms/quickstart>`__, `Wireless SIM
    <https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands>`__, `short code
    <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, or `channel address
    <https://www.twilio.com/docs/messaging/channels>`__ (e.g., ``whatsapp:+15554449999``). For incoming messages, this
    is the number or channel address of the sender. For outgoing messages, this value is a Twilio phone number,
    alphanumeric sender ID, short code, or channel address from which the message is sent."""

    to: OptionalNullable[str] = UNSET
    """The recipient's phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format) or `channel address
    <https://www.twilio.com/docs/messaging/channels>`__ (e.g. ``whatsapp:+15552229999``)"""

    date_updated: OptionalNullable[str] = UNSET
    """The `RFC 2822 <https://datatracker.ietf.org/doc/html/rfc2822#section-3.3>`__ timestamp (in GMT) of when the
    Message resource was last updated"""

    price: OptionalNullable[str] = UNSET
    """The amount billed for the message in the currency specified by ``price_unit``. The ``price`` is populated after
    the message has been sent/received, and may not be immediately availalble. View the `Pricing page
    <https://www.twilio.com/en-us/pricing>`__ for more details."""

    error_message: OptionalNullable[str] = UNSET
    """The description of the ``error_code`` if the Message ``status`` is ``failed`` or ``undelivered``. If no error was
    encountered, the value is ``null``. The value returned in this field for a specific error cause is subject to change
    as Twilio improves errors. Users should not use the ``error_code`` and ``error_message`` fields programmatically."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the Message resource, relative to ``https://api.twilio.com``."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the Message resource"""

    num_media: OptionalNullable[str] = UNSET
    """The number of media files associated with the Message resource."""

    status: Optional[MessageEnumStatusOrStr] = UNSET
    """The status of the Message. Possible values: ``accepted``, ``scheduled``, ``canceled``, ``queued``, ``sending``,
    ``sent``, ``failed``, ``delivered``, ``undelivered``, ``receiving``, ``received``, or ``read`` (WhatsApp only). For
    more information, See `detailed descriptions
    <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__."""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/api/service-resource>`__ associated with
    the Message resource. A unique default value is assigned if a Messaging Service is not used."""

    sid: OptionalNullable[str] = UNSET
    """The unique, Twilio-provided string that identifies the Message resource."""

    date_sent: OptionalNullable[str] = UNSET
    """The `RFC 2822 <https://datatracker.ietf.org/doc/html/rfc2822#section-3.3>`__ timestamp (in GMT) of when the
    Message was sent. For an outgoing message, this is when Twilio sent the message. For an incoming message, this is
    when Twilio sent the HTTP request to your incoming message webhook URL."""

    date_created: OptionalNullable[str] = UNSET
    """The `RFC 2822 <https://datatracker.ietf.org/doc/html/rfc2822#section-3.3>`__ timestamp (in GMT) of when the
    Message resource was created"""

    error_code: OptionalNullable[int] = UNSET
    """The `error code <https://www.twilio.com/docs/api/errors>`__ returned if the Message ``status`` is ``failed`` or
    ``undelivered``. If no error was encountered, the value is ``null``. The value returned in this field for a specific
    error cause is subject to change as Twilio improves errors. Users should not use the ``error_code`` and
    ``error_message`` fields programmatically."""

    price_unit: OptionalNullable[str] = UNSET
    """The currency in which ``price`` is measured, in `ISO 4127
    <https://www.iso.org/iso/home/standards/currency_codes.htm>`__ format (e.g. ``usd``, ``eur``, ``jpy``)."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to process the Message"""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related resources identified by their URIs relative to ``https://api.twilio.com``"""


class ApiV2010AccountMessageDict(TypedDict):
    body: NotRequired[str | None]
    num_segments: NotRequired[str | None]
    direction: NotRequired[MessageEnumDirectionOrStr]
    from_: NotRequired[str | None]
    to: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    price: NotRequired[str | None]
    error_message: NotRequired[str | None]
    uri: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    num_media: NotRequired[str | None]
    status: NotRequired[MessageEnumStatusOrStr]
    messaging_service_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    date_sent: NotRequired[str | None]
    date_created: NotRequired[str | None]
    error_code: NotRequired[int | None]
    price_unit: NotRequired[str | None]
    api_version: NotRequired[str | None]
    subresource_uris: NotRequired[Any | None]
