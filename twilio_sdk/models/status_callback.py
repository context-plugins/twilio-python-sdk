from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.method11 import Method11OrStr


class StatusCallback(SdkBaseModel):
    url: AnyUrl
    """The destination URL for webhooks."""

    method: Optional[Method11OrStr] = UNSET
    """The HTTP method used to invoke the webhook URL."""


class StatusCallbackDict(TypedDict):
    url: AnyUrl
    method: NotRequired[Method11OrStr]
