from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ContentApprovalRequest(SdkBaseModel):
    """Content approval request body"""

    name: str
    """Name of the template."""

    category: str
    """A WhatsApp recognized template category."""


class ContentApprovalRequestDict(TypedDict):
    name: str
    category: str
