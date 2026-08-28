from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Capabilities2(SdkBaseModel):
    """Set of booleans describing the capabilities hosted on Twilio's platform. SMS is currently only supported."""

    mms: Optional[bool] = UNSET
    sms: Optional[bool] = UNSET
    voice: Optional[bool] = UNSET


class Capabilities2Dict(TypedDict):
    mms: NotRequired[bool]
    sms: NotRequired[bool]
    voice: NotRequired[bool]
