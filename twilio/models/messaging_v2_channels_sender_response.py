from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.channels_sender_enum_status import ChannelsSenderEnumStatusOrStr
from .messaging_v2_channels_sender_configuration import (
    MessagingV2ChannelsSenderConfiguration,
    MessagingV2ChannelsSenderConfigurationDict,
)
from .messaging_v2_channels_sender_offline_reasons_items import (
    MessagingV2ChannelsSenderOfflineReasonsItems,
    MessagingV2ChannelsSenderOfflineReasonsItemsDict,
)
from .messaging_v2_channels_sender_profile_generic_response import (
    MessagingV2ChannelsSenderProfileGenericResponse,
    MessagingV2ChannelsSenderProfileGenericResponseDict,
)
from .messaging_v2_channels_sender_properties import (
    MessagingV2ChannelsSenderProperties,
    MessagingV2ChannelsSenderPropertiesDict,
)
from .messaging_v2_channels_sender_webhook import MessagingV2ChannelsSenderWebhook, MessagingV2ChannelsSenderWebhookDict
from .messaging_v2_rcs_compliance_response import MessagingV2RcsComplianceResponse, MessagingV2RcsComplianceResponseDict


class MessagingV2ChannelsSenderResponse(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The SID of the sender."""

    status: Optional[ChannelsSenderEnumStatusOrStr] = UNSET
    """The status of the sender."""

    sender_id: OptionalNullable[str] = UNSET
    """The ID of the sender in ``whatsapp:<E.164_PHONE_NUMBER>`` format."""

    configuration: OptionalNullable[MessagingV2ChannelsSenderConfiguration] = UNSET
    """The configuration settings for creating a sender."""

    webhook: OptionalNullable[MessagingV2ChannelsSenderWebhook] = UNSET
    """The configuration settings for webhooks."""

    profile: OptionalNullable[MessagingV2ChannelsSenderProfileGenericResponse] = UNSET
    """The profile information for the sender."""

    properties: OptionalNullable[MessagingV2ChannelsSenderProperties] = UNSET
    """The additional properties for the sender."""

    offline_reasons: OptionalNullable[list[MessagingV2ChannelsSenderOfflineReasonsItems | None]] = UNSET
    """The reasons why the sender is offline."""

    compliance: OptionalNullable[MessagingV2RcsComplianceResponse] = UNSET
    """The KYC compliance information. This section consists of response to the request launch."""

    url: OptionalNullable[str] = UNSET
    """The URL of the resource."""


class MessagingV2ChannelsSenderResponseDict(TypedDict):
    sid: NotRequired[str | None]
    status: NotRequired[ChannelsSenderEnumStatusOrStr]
    sender_id: NotRequired[str | None]
    configuration: NotRequired[
        MessagingV2ChannelsSenderConfiguration | MessagingV2ChannelsSenderConfigurationDict | None
    ]
    webhook: NotRequired[MessagingV2ChannelsSenderWebhook | MessagingV2ChannelsSenderWebhookDict | None]
    profile: NotRequired[
        MessagingV2ChannelsSenderProfileGenericResponse | MessagingV2ChannelsSenderProfileGenericResponseDict | None
    ]
    properties: NotRequired[MessagingV2ChannelsSenderProperties | MessagingV2ChannelsSenderPropertiesDict | None]
    offline_reasons: NotRequired[
        (
            list[MessagingV2ChannelsSenderOfflineReasonsItems | MessagingV2ChannelsSenderOfflineReasonsItemsDict | None]
            | None
        )
    ]
    compliance: NotRequired[MessagingV2RcsComplianceResponse | MessagingV2RcsComplianceResponseDict | None]
    url: NotRequired[str | None]
