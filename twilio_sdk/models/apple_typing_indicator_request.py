from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.event import EventOrStr


class AppleTypingIndicatorRequest(SdkBaseModel):
    """Typing indicator request for Apple Messages for Business channel."""

    channel: Literal["APPLE"] = "APPLE"
    """The messaging channel. Must be "APPLE"."""

    from_: str = Field(alias="from")
    """The Apple Messages for Business identifier of the sender (business)."""

    to: str
    """The Apple Messages for Business identifier of the recipient (customer)."""

    event: Optional[EventOrStr] = UNSET
    """The type of typing event. "START" indicates the agent began typing, "END" indicates the agent stopped typing.
    Defaults to "START"."""


class AppleTypingIndicatorRequestDict(TypedDict):
    channel: NotRequired[Literal["APPLE"]]
    from_: str
    to: str
    event: NotRequired[EventOrStr]
