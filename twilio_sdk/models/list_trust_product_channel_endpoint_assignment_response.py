from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_trust_product_trust_product_channel_endpoint_assignment import (
    TrusthubV1TrustProductTrustProductChannelEndpointAssignment,
    TrusthubV1TrustProductTrustProductChannelEndpointAssignmentDict,
)


class ListTrustProductChannelEndpointAssignmentResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1TrustProductTrustProductChannelEndpointAssignment]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTrustProductChannelEndpointAssignmentResponseDict(TypedDict):
    results: NotRequired[
        list[
            (
                TrusthubV1TrustProductTrustProductChannelEndpointAssignment
                | TrusthubV1TrustProductTrustProductChannelEndpointAssignmentDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
