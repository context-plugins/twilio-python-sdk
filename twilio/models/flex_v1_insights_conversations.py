from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FlexV1InsightsConversations(SdkBaseModel):
    account_id: OptionalNullable[str] = UNSET
    """The id of the account."""

    conversation_id: OptionalNullable[str] = UNSET
    """The unique id of the conversation"""

    segment_count: Optional[int] = UNSET
    """The count of segments for a conversation"""

    segments: Optional[list[Any | None]] = UNSET
    """The Segments of a conversation"""


class FlexV1InsightsConversationsDict(TypedDict):
    account_id: NotRequired[str | None]
    conversation_id: NotRequired[str | None]
    segment_count: NotRequired[int]
    segments: NotRequired[list[Any | None]]
