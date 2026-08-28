from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_customer_profile_customer_profile_channel_endpoint_assignment import (
    TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment,
    TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignmentDict,
)


class ListCustomerProfileChannelEndpointAssignmentResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCustomerProfileChannelEndpointAssignmentResponseDict(TypedDict):
    results: NotRequired[
        list[
            (
                TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment
                | TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignmentDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
