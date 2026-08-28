from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ConversationsV1User(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the User resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the User resource."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User
    resource is associated with."""

    role_sid: OptionalNullable[str] = UNSET
    """The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__ assigned to the
    user."""

    identity: OptionalNullable[str] = UNSET
    """The application-defined string that uniquely identifies the resource's User within the `Conversation Service
    <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is often a username or an email
    address, and is case-sensitive."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    attributes: OptionalNullable[str] = UNSET
    """The JSON Object string that stores application-specific data. If attributes have not been set, ``{}`` is
    returned."""

    is_online: OptionalNullable[bool] = UNSET
    """Whether the User is actively connected to this Conversations Service and online. This value is only returned by
    Fetch actions that return a single resource and ``null`` is always returned by a Read action. This value is ``null``
    if the Service's ``reachability_enabled`` is ``false``, if the User has never been online for this Conversations
    Service, even if the Service's ``reachability_enabled`` is ``true``."""

    is_notifiable: OptionalNullable[bool] = UNSET
    """Whether the User has a potentially valid Push Notification registration (APN or GCM) for this Conversations
    Service. If at least one registration exists, ``true``; otherwise ``false``. This value is only returned by Fetch
    actions that return a single resource and ``null`` is always returned by a Read action. This value is ``null`` if
    the Service's ``reachability_enabled`` is ``false``, and if the User has never had a notification registration, even
    if the Service's ``reachability_enabled`` is ``true``."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this user."""

    links: OptionalNullable[Any] = UNSET


class ConversationsV1UserDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    role_sid: NotRequired[str | None]
    identity: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    attributes: NotRequired[str | None]
    is_online: NotRequired[bool | None]
    is_notifiable: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
