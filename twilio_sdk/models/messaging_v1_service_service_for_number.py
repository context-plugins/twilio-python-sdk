from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MessagingV1ServiceServiceForNumber(SdkBaseModel):
    number_sid: OptionalNullable[str] = UNSET
    """The SID to identify the number resource."""

    sid: OptionalNullable[str] = UNSET
    """The SID of the messaging service that the phone number is in."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the messaging service resource."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Service resource."""


class MessagingV1ServiceServiceForNumberDict(TypedDict):
    number_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
