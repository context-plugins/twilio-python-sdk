from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MessagingV2ChannelsSenderOfflineReasonsItems(SdkBaseModel):
    code: OptionalNullable[str] = UNSET
    """The error code."""

    message: OptionalNullable[str] = UNSET
    """The error message."""

    more_info: OptionalNullable[AnyUrl] = UNSET
    """The URL to get more information about the error."""


class MessagingV2ChannelsSenderOfflineReasonsItemsDict(TypedDict):
    code: NotRequired[str | None]
    message: NotRequired[str | None]
    more_info: NotRequired[AnyUrl | None]
