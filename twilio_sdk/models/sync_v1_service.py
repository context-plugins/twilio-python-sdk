from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SyncV1Service(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Service resource."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. It can be used in place of the resource's
    ``sid`` in the URL to address the resource. It is a read-only property, it cannot be assigned using REST API."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Service resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Service resource."""

    webhook_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when Sync objects are manipulated."""

    webhooks_from_rest_enabled: OptionalNullable[bool] = UNSET
    """Whether the Service instance should call ``webhook_url`` when the REST API is used to update Sync objects. The
    default is ``false``."""

    reachability_webhooks_enabled: OptionalNullable[bool] = UNSET
    """Whether the service instance calls ``webhook_url`` when client endpoints connect to Sync. The default is
    ``false``."""

    acl_enabled: OptionalNullable[bool] = UNSET
    """Whether token identities in the Service must be granted access to Sync objects by using the `Permissions
    <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource. It is disabled (false) by default."""

    reachability_debouncing_enabled: OptionalNullable[bool] = UNSET
    """Whether every ``endpoint_disconnected`` event should occur after a configurable delay. The default is ``false``,
    where the ``endpoint_disconnected`` event occurs immediately after disconnection. When ``true``, intervening
    reconnections can prevent the ``endpoint_disconnected`` event."""

    reachability_debouncing_window: Optional[int] = UNSET
    """The reachability event delay in milliseconds if ``reachability_debouncing_enabled`` = ``true``. Must be between
    1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client
    disconnects, and a Sync identity is declared offline, before ``webhook_url`` is called, if all endpoints remain
    offline. A reconnection from the same identity by any endpoint during this interval prevents the reachability event
    from occurring."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class SyncV1ServiceDict(TypedDict):
    sid: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    webhook_url: NotRequired[AnyUrl | None]
    webhooks_from_rest_enabled: NotRequired[bool | None]
    reachability_webhooks_enabled: NotRequired[bool | None]
    acl_enabled: NotRequired[bool | None]
    reachability_debouncing_enabled: NotRequired[bool | None]
    reachability_debouncing_window: NotRequired[int]
    links: NotRequired[Any | None]
