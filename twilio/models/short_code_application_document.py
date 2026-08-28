from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.document_type import DocumentTypeOrStr


class ShortCodeApplicationDocument(SdkBaseModel):
    sid: Optional[str] = UNSET
    """The unique identifier of the document."""

    document_type: Optional[DocumentTypeOrStr] = UNSET
    """The type of document."""

    friendly_name: Optional[str] = UNSET
    """The friendly name of the document."""


class ShortCodeApplicationDocumentDict(TypedDict):
    sid: NotRequired[str]
    document_type: NotRequired[DocumentTypeOrStr]
    friendly_name: NotRequired[str]
