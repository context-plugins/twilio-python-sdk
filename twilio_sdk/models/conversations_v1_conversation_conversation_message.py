from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ConversationsV1ConversationConversationMessage(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this message."""

    conversation_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Conversation <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for
    this message."""

    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    index: Optional[int] = UNSET
    """The index of the message within the `Conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__. Indices may skip numbers, but will always
    be in order of when the message was received."""

    author: OptionalNullable[str] = UNSET
    """The channel specific identifier of the message's author. Defaults to ``system``."""

    body: OptionalNullable[str] = UNSET
    """The content of the message, can be up to 1,600 characters long."""

    media: Optional[list[Any | None]] = UNSET
    """An array of objects that describe the Message's media, if the message contains media. Each object contains these
    fields: ``content_type`` with the MIME type of the media, ``filename`` with the name of the media, ``sid`` with the
    SID of the Media resource, and ``size`` with the media object's file size in bytes. If the Message has no media,
    this value is ``null``."""

    attributes: OptionalNullable[str] = UNSET
    """A string metadata field you can use to store any data you wish. The string value must contain structurally valid
    JSON if specified. **Note** that if the attributes are not set "{}" will be returned."""

    participant_sid: OptionalNullable[str] = UNSET
    """The unique ID of messages's author participant. Null in case of ``system`` sent message."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated. ``null`` if the message has not been edited."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource API URL for this message."""

    delivery: OptionalNullable[Any] = UNSET
    """An object that contains the summary of delivery statuses for the message to non-chat participants."""

    links: OptionalNullable[Any] = UNSET
    """Contains an absolute API resource URL to access the delivery & read receipts of this message."""

    content_sid: OptionalNullable[str] = UNSET
    """The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__ template."""


class ConversationsV1ConversationConversationMessageDict(TypedDict):
    account_sid: NotRequired[str | None]
    conversation_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    index: NotRequired[int]
    author: NotRequired[str | None]
    body: NotRequired[str | None]
    media: NotRequired[list[Any | None]]
    attributes: NotRequired[str | None]
    participant_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    delivery: NotRequired[Any | None]
    links: NotRequired[Any | None]
    content_sid: NotRequired[str | None]
