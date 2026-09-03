from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_configuration_address import (
    ConversationsV1ConfigurationAddress,
    ConversationsV1ConfigurationAddressDict,
)
from .meta import Meta, MetaDict


class ListConfigurationAddressResponse(SdkBaseModel):
    address_configurations: Optional[list[ConversationsV1ConfigurationAddress]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConfigurationAddressResponseDict(TypedDict):
    address_configurations: NotRequired[
        list[ConversationsV1ConfigurationAddress | ConversationsV1ConfigurationAddressDict]
    ]
    meta: NotRequired[Meta | MetaDict]
