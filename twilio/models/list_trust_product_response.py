from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_trust_product import TrusthubV1TrustProduct, TrusthubV1TrustProductDict


class ListTrustProductResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1TrustProduct]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTrustProductResponseDict(TypedDict):
    results: NotRequired[list[TrusthubV1TrustProduct | TrusthubV1TrustProductDict]]
    meta: NotRequired[Meta | MetaDict]
