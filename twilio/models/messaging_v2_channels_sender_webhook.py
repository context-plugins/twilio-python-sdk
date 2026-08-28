from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.callback_method2 import CallbackMethod2OrStr
from .enums.fallback_method1 import FallbackMethod1OrStr


class MessagingV2ChannelsSenderWebhook(SdkBaseModel):
    """The configuration settings for webhooks."""

    callback_url: OptionalNullable[str] = UNSET
    """The URL to send the webhook to."""

    callback_method: OptionalNullable[CallbackMethod2OrStr] = UNSET
    """The HTTP method for the webhook."""

    fallback_url: OptionalNullable[str] = UNSET
    """The URL to send the fallback webhook to."""

    fallback_method: OptionalNullable[FallbackMethod1OrStr] = UNSET
    """The HTTP method for the fallback webhook."""

    status_callback_url: OptionalNullable[str] = UNSET
    """The URL to send the status callback to."""

    status_callback_method: OptionalNullable[str] = UNSET
    """The HTTP method for the status callback."""


class MessagingV2ChannelsSenderWebhookDict(TypedDict):
    callback_url: NotRequired[str | None]
    callback_method: NotRequired[CallbackMethod2OrStr | None]
    fallback_url: NotRequired[str | None]
    fallback_method: NotRequired[FallbackMethod1OrStr | None]
    status_callback_url: NotRequired[str | None]
    status_callback_method: NotRequired[str | None]
