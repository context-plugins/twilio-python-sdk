from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.conversation_message_receipt_enum_delivery_status import ConversationMessageReceiptEnumDeliveryStatusOrStr


class ConversationsV1ConversationConversationMessageConversationMessageReceipt(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    participant."""

    conversation_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for
    this message."""

    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    message_sid: OptionalNullable[str] = UNSET
    """The SID of the message within a `Conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs to"""

    channel_message_sid: OptionalNullable[str] = UNSET
    """A messaging channel-specific identifier for the message delivered to participant e.g. ``SMxx`` for SMS, ``WAxx``
    for Whatsapp etc."""

    participant_sid: OptionalNullable[str] = UNSET
    """The unique ID of the participant the delivery receipt belongs to."""

    status: Optional[ConversationMessageReceiptEnumDeliveryStatusOrStr] = UNSET
    """The message delivery status, can be ``read``, ``failed``, ``delivered``, ``undelivered``, ``sent`` or null."""

    error_code: Optional[int] = UNSET
    """The message `delivery error code
    <https://www.twilio.com/docs/sms/api/message-resource#delivery-related-errors>`__ for a ``failed`` status,"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated. ``null`` if the delivery receipt has not been updated."""

    url: OptionalNullable[str] = UNSET
    """An absolute API resource URL for this delivery receipt."""


class ConversationsV1ConversationConversationMessageConversationMessageReceiptDict(TypedDict):
    account_sid: NotRequired[str | None]
    conversation_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    message_sid: NotRequired[str | None]
    channel_message_sid: NotRequired[str | None]
    participant_sid: NotRequired[str | None]
    status: NotRequired[ConversationMessageReceiptEnumDeliveryStatusOrStr]
    error_code: NotRequired[int]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
