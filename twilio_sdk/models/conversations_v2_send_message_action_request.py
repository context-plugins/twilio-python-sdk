from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .conversations_v2_send_message_payload import (
    ConversationsV2SendMessagePayload,
    ConversationsV2SendMessagePayloadDict,
)


class ConversationsV2SendMessageActionRequest(SdkBaseModel):
    type_: str = Field(alias="type")
    """Action type discriminator. Accepted values: SEND_MESSAGE."""

    payload: ConversationsV2SendMessagePayload


class ConversationsV2SendMessageActionRequestDict(TypedDict):
    type_: str
    payload: ConversationsV2SendMessagePayload | ConversationsV2SendMessagePayloadDict
