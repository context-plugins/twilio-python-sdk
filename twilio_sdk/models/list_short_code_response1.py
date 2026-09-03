from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_service_short_code import MessagingV1ServiceShortCode, MessagingV1ServiceShortCodeDict
from .meta import Meta, MetaDict


class ListShortCodeResponse1(SdkBaseModel):
    short_codes: Optional[list[MessagingV1ServiceShortCode]] = UNSET
    meta: Optional[Meta] = UNSET


class ListShortCodeResponse1Dict(TypedDict):
    short_codes: NotRequired[list[MessagingV1ServiceShortCode | MessagingV1ServiceShortCodeDict]]
    meta: NotRequired[Meta | MetaDict]
