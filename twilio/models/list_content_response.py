from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_v1_content import ContentV1Content, ContentV1ContentDict
from .meta import Meta, MetaDict


class ListContentResponse(SdkBaseModel):
    contents: Optional[list[ContentV1Content]] = UNSET
    meta: Optional[Meta] = UNSET


class ListContentResponseDict(TypedDict):
    contents: NotRequired[list[ContentV1Content | ContentV1ContentDict]]
    meta: NotRequired[Meta | MetaDict]
