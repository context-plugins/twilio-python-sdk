from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.method11 import Method11OrStr


class StatusCallback(SdkBaseModel):
    url: str
    """The destination URL for webhooks."""

    method: Optional[Method11OrStr] = UNSET
    """The HTTP method used to invoke the webhook URL."""


class StatusCallbackDict(TypedDict):
    url: str
    method: NotRequired[Method11OrStr]
