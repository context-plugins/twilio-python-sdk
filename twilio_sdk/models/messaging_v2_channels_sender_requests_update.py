from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .messaging_v2_channels_sender_configuration import (
    MessagingV2ChannelsSenderConfiguration,
    MessagingV2ChannelsSenderConfigurationDict,
)
from .messaging_v2_channels_sender_profile import MessagingV2ChannelsSenderProfile, MessagingV2ChannelsSenderProfileDict
from .messaging_v2_channels_sender_webhook import MessagingV2ChannelsSenderWebhook, MessagingV2ChannelsSenderWebhookDict


class MessagingV2ChannelsSenderRequestsUpdate(SdkBaseModel):
    configuration: OptionalNullable[MessagingV2ChannelsSenderConfiguration] = UNSET
    """The configuration settings for creating a sender."""

    webhook: OptionalNullable[MessagingV2ChannelsSenderWebhook] = UNSET
    """The configuration settings for webhooks."""

    profile: OptionalNullable[MessagingV2ChannelsSenderProfile] = UNSET
    """The profile information for the sender."""


class MessagingV2ChannelsSenderRequestsUpdateDict(TypedDict):
    configuration: NotRequired[
        MessagingV2ChannelsSenderConfiguration | MessagingV2ChannelsSenderConfigurationDict | None
    ]
    webhook: NotRequired[MessagingV2ChannelsSenderWebhook | MessagingV2ChannelsSenderWebhookDict | None]
    profile: NotRequired[MessagingV2ChannelsSenderProfile | MessagingV2ChannelsSenderProfileDict | None]
