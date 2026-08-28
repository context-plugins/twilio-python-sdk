from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_supporting_document import TrusthubV1SupportingDocument, TrusthubV1SupportingDocumentDict


class ListSupportingDocumentResponse1(SdkBaseModel):
    results: Optional[list[TrusthubV1SupportingDocument]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSupportingDocumentResponse1Dict(TypedDict):
    results: NotRequired[list[TrusthubV1SupportingDocument | TrusthubV1SupportingDocumentDict]]
    meta: NotRequired[Meta | MetaDict]
