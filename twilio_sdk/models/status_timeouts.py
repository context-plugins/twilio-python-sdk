from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StatusTimeouts(SdkBaseModel):
    inactive: Optional[int] = UNSET
    """The inactivity timeout in minutes. For more information, see `Conversation lifecycle
    </docs/platform/conversations/concepts/lifecycle>`__."""

    closed: Optional[int] = UNSET
    """The close timeout in minutes. For more information, see `Conversation lifecycle
    </docs/platform/conversations/concepts/lifecycle>`__."""


class StatusTimeoutsDict(TypedDict):
    inactive: NotRequired[int]
    closed: NotRequired[int]
