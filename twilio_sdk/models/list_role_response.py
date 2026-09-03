from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_role import ConversationsV1Role, ConversationsV1RoleDict
from .meta import Meta, MetaDict


class ListRoleResponse(SdkBaseModel):
    roles: Optional[list[ConversationsV1Role]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRoleResponseDict(TypedDict):
    roles: NotRequired[list[ConversationsV1Role | ConversationsV1RoleDict]]
    meta: NotRequired[Meta | MetaDict]
