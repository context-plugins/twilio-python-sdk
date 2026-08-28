from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ConversationsV1ServiceServiceConfiguration(SdkBaseModel):
    chat_service_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Service configuration resource."""

    default_conversation_creator_role_sid: OptionalNullable[str] = UNSET
    """The conversation-level role assigned to a conversation creator when they join a new conversation. See
    `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info about roles."""

    default_conversation_role_sid: OptionalNullable[str] = UNSET
    """The conversation-level role assigned to users when they are added to a conversation. See `Conversation Role
    <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info about roles."""

    default_chat_service_role_sid: OptionalNullable[str] = UNSET
    """The service-level role assigned to users when they are added to the service. See `Conversation Role
    <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info about roles."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this service configuration."""

    links: OptionalNullable[Any] = UNSET
    """Contains an absolute API resource URL to access the push notifications configuration of this service."""

    reachability_enabled: OptionalNullable[bool] = UNSET
    """Whether the `Reachability Indicator <https://www.twilio.com/docs/conversations/reachability>`__ is enabled for
    this Conversations Service. The default is ``false``."""


class ConversationsV1ServiceServiceConfigurationDict(TypedDict):
    chat_service_sid: NotRequired[str | None]
    default_conversation_creator_role_sid: NotRequired[str | None]
    default_conversation_role_sid: NotRequired[str | None]
    default_chat_service_role_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
    reachability_enabled: NotRequired[bool | None]
