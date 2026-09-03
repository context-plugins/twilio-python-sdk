from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_v1_content_and_approvals import ContentV1ContentAndApprovals, ContentV1ContentAndApprovalsDict
from .meta import Meta, MetaDict


class ListContentAndApprovalsResponse(SdkBaseModel):
    contents: Optional[list[ContentV1ContentAndApprovals]] = UNSET
    meta: Optional[Meta] = UNSET


class ListContentAndApprovalsResponseDict(TypedDict):
    contents: NotRequired[list[ContentV1ContentAndApprovals | ContentV1ContentAndApprovalsDict]]
    meta: NotRequired[Meta | MetaDict]
