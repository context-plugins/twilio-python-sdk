from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.status21 import Status21OrStr
from .error import Error, ErrorDict


class ConversationsV2OperationStatus(SdkBaseModel):
    """Status of a long-running operation."""

    operation_id: str = Field(alias="operationId")
    """Unique identifier for the long-running operation."""

    status: Status21OrStr
    """Current status of the operation."""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """Timestamp when the operation was created."""

    completed_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="completedAt")
    """Timestamp when the operation completed. Only present for completed or failed operations."""

    status_url: str = Field(alias="statusUrl")
    """URL to poll for operation status."""

    error: OptionalNullable[Error] = UNSET
    """Error details if the operation failed. Follows RFC 9457 Problem Details."""

    related: Optional[dict[str, str | None]] = UNSET
    """Named resource identifiers associated with this operation. Keys depend on the operation type:
    - config-create, config-update, config-delete: configurationId
    - conversation-delete: conversationId"""


class ConversationsV2OperationStatusDict(TypedDict):
    operation_id: str
    status: Status21OrStr
    created_at: RFC3339DateTime
    completed_at: NotRequired[RFC3339DateTime | None]
    status_url: str
    error: NotRequired[Error | ErrorDict | None]
    related: NotRequired[dict[str, str | None]]
