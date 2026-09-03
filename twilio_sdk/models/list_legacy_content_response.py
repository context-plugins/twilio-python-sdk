from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_v1_legacy_content import ContentV1LegacyContent, ContentV1LegacyContentDict
from .meta import Meta, MetaDict


class ListLegacyContentResponse(SdkBaseModel):
    contents: Optional[list[ContentV1LegacyContent]] = UNSET
    meta: Optional[Meta] = UNSET


class ListLegacyContentResponseDict(TypedDict):
    contents: NotRequired[list[ContentV1LegacyContent | ContentV1LegacyContentDict]]
    meta: NotRequired[Meta | MetaDict]
