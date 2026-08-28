from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_trust_product_trust_product_evaluation import (
    TrusthubV1TrustProductTrustProductEvaluation,
    TrusthubV1TrustProductTrustProductEvaluationDict,
)


class ListTrustProductEvaluationResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1TrustProductTrustProductEvaluation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTrustProductEvaluationResponseDict(TypedDict):
    results: NotRequired[
        list[TrusthubV1TrustProductTrustProductEvaluation | TrusthubV1TrustProductTrustProductEvaluationDict]
    ]
    meta: NotRequired[Meta | MetaDict]
