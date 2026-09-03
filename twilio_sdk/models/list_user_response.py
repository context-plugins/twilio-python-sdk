from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_user import ConversationsV1User, ConversationsV1UserDict
from .meta import Meta, MetaDict


class ListUserResponse(SdkBaseModel):
    users: Optional[list[ConversationsV1User]] = UNSET
    meta: Optional[Meta] = UNSET


class ListUserResponseDict(TypedDict):
    users: NotRequired[list[ConversationsV1User | ConversationsV1UserDict]]
    meta: NotRequired[Meta | MetaDict]
