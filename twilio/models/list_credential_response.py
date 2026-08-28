from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_credential import ConversationsV1Credential, ConversationsV1CredentialDict
from .meta import Meta, MetaDict


class ListCredentialResponse(SdkBaseModel):
    credentials: Optional[list[ConversationsV1Credential]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCredentialResponseDict(TypedDict):
    credentials: NotRequired[list[ConversationsV1Credential | ConversationsV1CredentialDict]]
    meta: NotRequired[Meta | MetaDict]
