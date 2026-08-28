from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_brand_registrations_brand_vetting import (
    MessagingV1BrandRegistrationsBrandVetting,
    MessagingV1BrandRegistrationsBrandVettingDict,
)
from .meta import Meta, MetaDict


class ListBrandVettingResponse(SdkBaseModel):
    data: Optional[list[MessagingV1BrandRegistrationsBrandVetting]] = UNSET
    meta: Optional[Meta] = UNSET


class ListBrandVettingResponseDict(TypedDict):
    data: NotRequired[list[MessagingV1BrandRegistrationsBrandVetting | MessagingV1BrandRegistrationsBrandVettingDict]]
    meta: NotRequired[Meta | MetaDict]
