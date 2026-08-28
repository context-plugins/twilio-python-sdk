from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsV2ConversationsV1Bridge(SdkBaseModel):
    """Configuration for Conversations V1 bridge. When set, messaging channels route through Conversations V1. Use this
    to integrate with existing Conversations V1 applications."""

    service_id: str = Field(alias="serviceId")
    """The Conversations V1 Service SID (IS prefix). One configuration per V1 Service SID."""


class ConversationsV2ConversationsV1BridgeDict(TypedDict):
    service_id: str
