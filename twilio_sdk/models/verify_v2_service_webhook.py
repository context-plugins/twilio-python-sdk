from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.webhook_enum_status import WebhookEnumStatusOrStr
from .enums.webhook_enum_version import WebhookEnumVersionOrStr


class VerifyV2ServiceWebhook(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Webhook resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Service."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Service resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the webhook. **This value should not contain PII.**"""

    event_types: Optional[list[str | None]] = UNSET
    """The array of events that this Webhook is subscribed to. Possible event types: ``*, factor.deleted,
    factor.created, factor.verified, challenge.approved, challenge.denied``"""

    status: Optional[WebhookEnumStatusOrStr] = UNSET
    """The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``"""

    version: Optional[WebhookEnumVersionOrStr] = UNSET
    """The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1`` is legacy and
    may be removed in the future."""

    webhook_url: OptionalNullable[AnyUrl] = UNSET
    """The URL associated with this Webhook."""

    webhook_method: Optional[AmdStatusCallbackMethodOrStr] = UNSET
    """The method to be used when calling the webhook's URL."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Webhook resource."""


class VerifyV2ServiceWebhookDict(TypedDict):
    sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    event_types: NotRequired[list[str | None]]
    status: NotRequired[WebhookEnumStatusOrStr]
    version: NotRequired[WebhookEnumVersionOrStr]
    webhook_url: NotRequired[AnyUrl | None]
    webhook_method: NotRequired[AmdStatusCallbackMethodOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
