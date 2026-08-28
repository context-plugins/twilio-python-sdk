from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.service_role_enum_role_type import ServiceRoleEnumRoleTypeOrStr


class ConversationsV1ServiceServiceRole(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Role resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Role resource."""

    chat_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Role
    resource is associated with."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    type_: Optional[ServiceRoleEnumRoleTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of role. Can be: ``conversation`` for `Conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for `Conversation
    Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles."""

    permissions: Optional[list[str | None]] = UNSET
    """An array of the permissions the role has been granted."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this user role."""


class ConversationsV1ServiceServiceRoleDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    chat_service_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    type_: NotRequired[ServiceRoleEnumRoleTypeOrStr]
    permissions: NotRequired[list[str | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
