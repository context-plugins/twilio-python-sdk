from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.porting_webhook_configuration_delete_enum_webhook_type import (
    PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr,
)


class NumbersV1PortingWebhookConfigurationDelete(SdkBaseModel):
    url: OptionalNullable[str] = UNSET
    """The URL of the webhook configuration request"""

    webhook_type: Optional[PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr] = UNSET
    """The of the webhook type of the configuration to be deleted"""


class NumbersV1PortingWebhookConfigurationDeleteDict(TypedDict):
    url: NotRequired[str | None]
    webhook_type: NotRequired[PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr]
