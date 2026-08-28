from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_conversation_conversation_message_conversation_message_receipt import (
    ConversationsV1ConversationConversationMessageConversationMessageReceipt,
    ConversationsV1ConversationConversationMessageConversationMessageReceiptDict,
)
from .meta import Meta, MetaDict


class ListConversationMessageReceiptResponse(SdkBaseModel):
    delivery_receipts: Optional[list[ConversationsV1ConversationConversationMessageConversationMessageReceipt]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConversationMessageReceiptResponseDict(TypedDict):
    delivery_receipts: NotRequired[
        list[
            (
                ConversationsV1ConversationConversationMessageConversationMessageReceipt
                | ConversationsV1ConversationConversationMessageConversationMessageReceiptDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
