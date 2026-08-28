from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class NumbersV1PortingWebhookConfiguration(SdkBaseModel):
    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the webhook configuration request"""

    port_in_target_url: OptionalNullable[AnyUrl] = UNSET
    """The complete webhook url that will be called when a notification event for port in request or port in phone
    number happens"""

    port_out_target_url: OptionalNullable[AnyUrl] = UNSET
    """The complete webhook url that will be called when a notification event for a port out phone number happens."""

    notifications_of: Optional[list[str | None]] = UNSET
    """A list to filter what notification events to receive for this account and its sub accounts. If it is an empty
    list, then it means that there are no filters for the notifications events to send in each webhook and all events
    will get sent."""


class NumbersV1PortingWebhookConfigurationDict(TypedDict):
    url: NotRequired[AnyUrl | None]
    port_in_target_url: NotRequired[AnyUrl | None]
    port_out_target_url: NotRequired[AnyUrl | None]
    notifications_of: NotRequired[list[str | None]]
