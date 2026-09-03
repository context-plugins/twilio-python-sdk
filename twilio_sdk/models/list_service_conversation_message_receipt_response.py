from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .service_conversation_message_receipt import (
    ServiceConversationMessageReceipt,
    ServiceConversationMessageReceiptDict,
)


class ListServiceConversationMessageReceiptResponse(SdkBaseModel):
    delivery_receipts: Optional[list[ServiceConversationMessageReceipt]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceConversationMessageReceiptResponseDict(TypedDict):
    delivery_receipts: NotRequired[list[ServiceConversationMessageReceipt | ServiceConversationMessageReceiptDict]]
    meta: NotRequired[Meta | MetaDict]
