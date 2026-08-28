from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_authorization_document_dependent_hosted_number_order import (
    NumbersV2AuthorizationDocumentDependentHostedNumberOrder,
    NumbersV2AuthorizationDocumentDependentHostedNumberOrderDict,
)


class ListDependentHostedNumberOrderResponse(SdkBaseModel):
    items: Optional[list[NumbersV2AuthorizationDocumentDependentHostedNumberOrder]] = UNSET
    meta: Optional[Meta] = UNSET


class ListDependentHostedNumberOrderResponseDict(TypedDict):
    items: NotRequired[
        list[
            (
                NumbersV2AuthorizationDocumentDependentHostedNumberOrder
                | NumbersV2AuthorizationDocumentDependentHostedNumberOrderDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
