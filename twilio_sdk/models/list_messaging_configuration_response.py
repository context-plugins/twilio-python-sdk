from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service_messaging_configuration import (
    VerifyV2ServiceMessagingConfiguration,
    VerifyV2ServiceMessagingConfigurationDict,
)


class ListMessagingConfigurationResponse(SdkBaseModel):
    messaging_configurations: Optional[list[VerifyV2ServiceMessagingConfiguration]] = UNSET
    meta: Optional[Meta] = UNSET


class ListMessagingConfigurationResponseDict(TypedDict):
    messaging_configurations: NotRequired[
        list[VerifyV2ServiceMessagingConfiguration | VerifyV2ServiceMessagingConfigurationDict]
    ]
    meta: NotRequired[Meta | MetaDict]
