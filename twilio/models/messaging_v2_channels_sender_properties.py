from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MessagingV2ChannelsSenderProperties(SdkBaseModel):
    """The additional properties for the sender."""

    quality_rating: OptionalNullable[str] = UNSET
    """The quality rating of the sender."""

    messaging_limit: OptionalNullable[str] = UNSET
    """The messaging limit of the sender."""


class MessagingV2ChannelsSenderPropertiesDict(TypedDict):
    quality_rating: NotRequired[str | None]
    messaging_limit: NotRequired[str | None]
