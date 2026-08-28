from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountCallUserDefinedMessageSubscription(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the User Defined
    Messages."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined Message
    Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages."""

    sid: OptionalNullable[str] = UNSET
    """The SID that uniquely identifies this User Defined Message Subscription."""

    date_created: OptionalNullable[str] = UNSET
    """The date that this User Defined Message Subscription was created, given in RFC 2822 format."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the User Defined Message Subscription Resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountCallUserDefinedMessageSubscriptionDict(TypedDict):
    account_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    uri: NotRequired[str | None]
