from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_plugin_configuration_configured_plugin import (
    FlexV1PluginConfigurationConfiguredPlugin,
    FlexV1PluginConfigurationConfiguredPluginDict,
)
from .meta import Meta, MetaDict


class ListConfiguredPluginResponse(SdkBaseModel):
    plugins: Optional[list[FlexV1PluginConfigurationConfiguredPlugin]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConfiguredPluginResponseDict(TypedDict):
    plugins: NotRequired[
        list[FlexV1PluginConfigurationConfiguredPlugin | FlexV1PluginConfigurationConfiguredPluginDict]
    ]
    meta: NotRequired[Meta | MetaDict]
