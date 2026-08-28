from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .unions.messaging_v1_service_us_app_to_person_response import (
    MessagingV1ServiceUsAppToPersonResponse,
    MessagingV1ServiceUsAppToPersonResponseDict,
)


class ListUsAppToPersonResponse(SdkBaseModel):
    compliance: Optional[list[MessagingV1ServiceUsAppToPersonResponse]] = UNSET
    meta: Optional[Meta] = UNSET


class ListUsAppToPersonResponseDict(TypedDict):
    compliance: NotRequired[list[MessagingV1ServiceUsAppToPersonResponse | MessagingV1ServiceUsAppToPersonResponseDict]]
    meta: NotRequired[Meta | MetaDict]
