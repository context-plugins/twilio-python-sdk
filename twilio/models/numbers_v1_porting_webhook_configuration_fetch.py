from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class NumbersV1PortingWebhookConfigurationFetch(SdkBaseModel):
    url: OptionalNullable[str] = UNSET
    """The URL of the webhook configuration request"""

    port_in_target_url: OptionalNullable[str] = UNSET
    """The complete webhook url that will be called when a notification event for port in request or port in phone
    number happens"""

    port_out_target_url: OptionalNullable[str] = UNSET
    """The complete webhook url that will be called when a notification event for a port out phone number happens."""

    notifications_of: Optional[list[str | None]] = UNSET
    """A list to filter what notification events to receive for this account and its sub accounts. If it is an empty
    list, then it means that there are no filters for the notifications events to send in each webhook and all events
    will get sent."""

    port_in_target_date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """Creation date for the port in webhook configuration"""

    port_out_target_date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """Creation date for the port out webhook configuration"""


class NumbersV1PortingWebhookConfigurationFetchDict(TypedDict):
    url: NotRequired[str | None]
    port_in_target_url: NotRequired[str | None]
    port_out_target_url: NotRequired[str | None]
    notifications_of: NotRequired[list[str | None]]
    port_in_target_date_created: NotRequired[RFC3339DateTime | None]
    port_out_target_date_created: NotRequired[RFC3339DateTime | None]
