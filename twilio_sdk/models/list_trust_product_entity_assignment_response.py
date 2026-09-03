from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_trust_product_trust_product_entity_assignment import (
    TrusthubV1TrustProductTrustProductEntityAssignment,
    TrusthubV1TrustProductTrustProductEntityAssignmentDict,
)


class ListTrustProductEntityAssignmentResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1TrustProductTrustProductEntityAssignment]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTrustProductEntityAssignmentResponseDict(TypedDict):
    results: NotRequired[
        list[
            TrusthubV1TrustProductTrustProductEntityAssignment | TrusthubV1TrustProductTrustProductEntityAssignmentDict
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
