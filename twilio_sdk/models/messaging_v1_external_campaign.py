from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1ExternalCampaign(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies a US A2P Compliance resource ``QE2c6890da8086d771620e9b13fadeba0b``."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that the Campaign belongs to."""

    campaign_id: OptionalNullable[str] = UNSET
    """ID of the preregistered campaign."""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/api/service-resource>`__ that the
    resource is associated with."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""


class MessagingV1ExternalCampaignDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    campaign_id: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
