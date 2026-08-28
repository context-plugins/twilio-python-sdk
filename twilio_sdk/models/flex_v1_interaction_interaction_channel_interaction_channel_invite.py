from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InteractionInteractionChannelInteractionChannelInvite(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string created by Twilio to identify an Interaction Channel Invite resource."""

    interaction_sid: OptionalNullable[str] = UNSET
    """The Interaction SID for this Channel."""

    channel_sid: OptionalNullable[str] = UNSET
    """The Channel SID for this Invite."""

    routing: OptionalNullable[Any] = UNSET
    """A JSON object representing the routing rules for the Interaction Channel. See `Outbound SMS Example
    <https://www.twilio.com/docs/flex/developer/conversations/interactions-api/interactions#agent-initiated-outbound-interactions>`__
    for an example Routing object. The Interactions resource uses TaskRouter for all routing functionality.
     All attributes in the Routing object on your Interaction request body are added “as is” to the task. For a list of
        known attributes consumed by the Flex UI and/or Flex Insights, see `Known Task Attributes
        <https://www.twilio.com/docs/flex/developer/conversations/interactions-api#task-attributes>`__."""

    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InteractionInteractionChannelInteractionChannelInviteDict(TypedDict):
    sid: NotRequired[str | None]
    interaction_sid: NotRequired[str | None]
    channel_sid: NotRequired[str | None]
    routing: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
