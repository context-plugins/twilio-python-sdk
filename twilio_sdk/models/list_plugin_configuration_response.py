from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_plugin_configuration import FlexV1PluginConfiguration, FlexV1PluginConfigurationDict
from .meta import Meta, MetaDict


class ListPluginConfigurationResponse(SdkBaseModel):
    configurations: Optional[list[FlexV1PluginConfiguration]] = UNSET
    meta: Optional[Meta] = UNSET


class ListPluginConfigurationResponseDict(TypedDict):
    configurations: NotRequired[list[FlexV1PluginConfiguration | FlexV1PluginConfigurationDict]]
    meta: NotRequired[Meta | MetaDict]
