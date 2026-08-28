from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.porting_webhook_configuration_delete_enum_webhook_type import (
    PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr,
)


class NumbersV1PortingWebhookConfigurationDelete(SdkBaseModel):
    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the webhook configuration request"""

    webhook_type: Optional[PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr] = UNSET
    """The of the webhook type of the configuration to be deleted"""


class NumbersV1PortingWebhookConfigurationDeleteDict(TypedDict):
    url: NotRequired[AnyUrl | None]
    webhook_type: NotRequired[PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr]
