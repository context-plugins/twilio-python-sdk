from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV2WebChannel(SdkBaseModel):
    conversation_sid: OptionalNullable[str] = UNSET
    """The unique string representing the `Conversation resource
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ created."""

    identity: OptionalNullable[str] = UNSET
    """The unique string representing the User created and should be authorized to participate in the Conversation. For
    more details, see `User Identity & Access Tokens <https://www.twilio.com/docs/conversations/identity>`__."""


class FlexV2WebChannelDict(TypedDict):
    conversation_sid: NotRequired[str | None]
    identity: NotRequired[str | None]
