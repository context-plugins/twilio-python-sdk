from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service_webhook import VerifyV2ServiceWebhook, VerifyV2ServiceWebhookDict


class ListWebhookResponse(SdkBaseModel):
    webhooks: Optional[list[VerifyV2ServiceWebhook]] = UNSET
    meta: Optional[Meta] = UNSET


class ListWebhookResponseDict(TypedDict):
    webhooks: NotRequired[list[VerifyV2ServiceWebhook | VerifyV2ServiceWebhookDict]]
    meta: NotRequired[Meta | MetaDict]
