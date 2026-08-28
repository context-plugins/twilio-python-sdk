from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_user import (
    ConversationsV1ServiceServiceUser,
    ConversationsV1ServiceServiceUserDict,
)
from .meta import Meta, MetaDict


class ListServiceUserResponse(SdkBaseModel):
    users: Optional[list[ConversationsV1ServiceServiceUser]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceUserResponseDict(TypedDict):
    users: NotRequired[list[ConversationsV1ServiceServiceUser | ConversationsV1ServiceServiceUserDict]]
    meta: NotRequired[Meta | MetaDict]
