from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsV2OperationAccepted(SdkBaseModel):
    """Slim response for an accepted long-running operation."""

    status_url: str = Field(alias="statusUrl")
    """URL to poll for operation status."""

    related: Optional[dict[str, str | None]] = UNSET
    """Named resource identifiers associated with this operation. Keys depend on the operation type:
    - config-create, config-update, config-delete: configurationId
    - conversation-delete: conversationId"""


class ConversationsV2OperationAcceptedDict(TypedDict):
    status_url: str
    related: NotRequired[dict[str, str | None]]
