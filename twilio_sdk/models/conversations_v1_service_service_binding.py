from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.service_binding_enum_binding_type import ServiceBindingEnumBindingTypeOrStr


class ConversationsV1ServiceServiceBinding(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this binding."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ the
    Binding resource is associated with."""

    credential_sid: OptionalNullable[str] = UNSET
    """The SID of the `Credential <https://www.twilio.com/docs/conversations/api/credential-resource>`__ for the
    binding. See `push notification configuration <https://www.twilio.com/docs/chat/push-notification-configuration>`__
    for more info."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated."""

    endpoint: OptionalNullable[str] = UNSET
    """The unique endpoint identifier for the Binding. The format of this value depends on the ``binding_type``."""

    identity: OptionalNullable[str] = UNSET
    """The application-defined string that uniquely identifies the `Conversation User
    <https://www.twilio.com/docs/conversations/api/user-resource>`__ within the `Conversation Service
    <https://www.twilio.com/docs/conversations/api/service-resource>`__. See `access tokens
    <https://www.twilio.com/docs/conversations/create-tokens>`__ for more info."""

    binding_type: Optional[ServiceBindingEnumBindingTypeOrStr] = UNSET
    """The push technology to use for the Binding. Can be: ``apn``, ``gcm``, ``fcm``, or ``twilsock``. See `push
    notification configuration <https://www.twilio.com/docs/chat/push-notification-configuration>`__ for more info."""

    message_types: Optional[list[str | None]] = UNSET
    """The `Conversation message types <https://www.twilio.com/docs/chat/push-notification-configuration#push-types>`__
    the binding is subscribed to."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this binding."""


class ConversationsV1ServiceServiceBindingDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    credential_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    endpoint: NotRequired[str | None]
    identity: NotRequired[str | None]
    binding_type: NotRequired[ServiceBindingEnumBindingTypeOrStr]
    message_types: NotRequired[list[str | None]]
    url: NotRequired[AnyUrl | None]
