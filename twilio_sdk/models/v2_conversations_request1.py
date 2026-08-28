from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status7 import Status7OrStr


class V2ConversationsRequest1(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the Conversation."""

    status: Status7OrStr
    """The state of the Conversation."""


class V2ConversationsRequest1Dict(TypedDict):
    name: NotRequired[str]
    status: Status7OrStr
