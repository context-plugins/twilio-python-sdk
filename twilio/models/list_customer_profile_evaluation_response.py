from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_customer_profile_customer_profile_evaluation import (
    TrusthubV1CustomerProfileCustomerProfileEvaluation,
    TrusthubV1CustomerProfileCustomerProfileEvaluationDict,
)


class ListCustomerProfileEvaluationResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1CustomerProfileCustomerProfileEvaluation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCustomerProfileEvaluationResponseDict(TypedDict):
    results: NotRequired[
        list[
            TrusthubV1CustomerProfileCustomerProfileEvaluation | TrusthubV1CustomerProfileCustomerProfileEvaluationDict
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
