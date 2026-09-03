from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_brand_registrations import MessagingV1BrandRegistrations, MessagingV1BrandRegistrationsDict
from .meta import Meta, MetaDict


class ListBrandRegistrationsResponse(SdkBaseModel):
    data: Optional[list[MessagingV1BrandRegistrations]] = UNSET
    meta: Optional[Meta] = UNSET


class ListBrandRegistrationsResponseDict(TypedDict):
    data: NotRequired[list[MessagingV1BrandRegistrations | MessagingV1BrandRegistrationsDict]]
    meta: NotRequired[Meta | MetaDict]
