from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_insights_conversations import FlexV1InsightsConversations, FlexV1InsightsConversationsDict
from .meta import Meta, MetaDict


class ListInsightsConversationsResponse(SdkBaseModel):
    conversations: Optional[list[FlexV1InsightsConversations]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInsightsConversationsResponseDict(TypedDict):
    conversations: NotRequired[list[FlexV1InsightsConversations | FlexV1InsightsConversationsDict]]
    meta: NotRequired[Meta | MetaDict]
