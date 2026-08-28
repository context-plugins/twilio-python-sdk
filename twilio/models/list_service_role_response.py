from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_role import (
    ConversationsV1ServiceServiceRole,
    ConversationsV1ServiceServiceRoleDict,
)
from .meta import Meta, MetaDict


class ListServiceRoleResponse(SdkBaseModel):
    roles: Optional[list[ConversationsV1ServiceServiceRole]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceRoleResponseDict(TypedDict):
    roles: NotRequired[list[ConversationsV1ServiceServiceRole | ConversationsV1ServiceServiceRoleDict]]
    meta: NotRequired[Meta | MetaDict]
