from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status11 import Status11OrStr


class ConversationsV2Action(SdkBaseModel):
    id: str
    """Unique identifier for this Action."""

    type_: str = Field(alias="type")
    """The type of action. Accepted values: SEND_MESSAGE."""

    status: Status11OrStr
    """Current status of the Action.
    - PENDING: Action accepted, awaiting downstream confirmation
    - COMPLETED: Downstream backend confirmed the action
    - FAILED: Downstream backend reported a failure"""

    conversation_id: str = Field(alias="conversationId")
    """The conversation this action belongs to."""

    related: Optional[dict[str, str]] = UNSET
    """Named identifiers from downstream. For SEND_MESSAGE:
    - messageSid: The downstream message SID (present when PENDING or COMPLETED)
    - communicationId: The Communication ID (present when COMPLETED)"""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """Timestamp when the action was created."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Timestamp when the action was last updated."""

    completed_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="completedAt")
    """Timestamp when the action reached a terminal status."""


class ConversationsV2ActionDict(TypedDict):
    id: str
    type_: str
    status: Status11OrStr
    conversation_id: str
    related: NotRequired[dict[str, str]]
    created_at: RFC3339DateTime
    updated_at: NotRequired[RFC3339DateTime]
    completed_at: NotRequired[RFC3339DateTime]
