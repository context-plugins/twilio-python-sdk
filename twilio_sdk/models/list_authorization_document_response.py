from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_authorization_document import NumbersV2AuthorizationDocument, NumbersV2AuthorizationDocumentDict


class ListAuthorizationDocumentResponse(SdkBaseModel):
    items: Optional[list[NumbersV2AuthorizationDocument]] = UNSET
    meta: Optional[Meta] = UNSET


class ListAuthorizationDocumentResponseDict(TypedDict):
    items: NotRequired[list[NumbersV2AuthorizationDocument | NumbersV2AuthorizationDocumentDict]]
    meta: NotRequired[Meta | MetaDict]
