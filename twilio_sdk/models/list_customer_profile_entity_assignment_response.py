from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_customer_profile_customer_profile_entity_assignment import (
    TrusthubV1CustomerProfileCustomerProfileEntityAssignment,
    TrusthubV1CustomerProfileCustomerProfileEntityAssignmentDict,
)


class ListCustomerProfileEntityAssignmentResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1CustomerProfileCustomerProfileEntityAssignment]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCustomerProfileEntityAssignmentResponseDict(TypedDict):
    results: NotRequired[
        list[
            (
                TrusthubV1CustomerProfileCustomerProfileEntityAssignment
                | TrusthubV1CustomerProfileCustomerProfileEntityAssignmentDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
