from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_plugin_plugin_version import FlexV1PluginPluginVersion, FlexV1PluginPluginVersionDict
from .meta import Meta, MetaDict


class ListPluginVersionResponse(SdkBaseModel):
    plugin_versions: Optional[list[FlexV1PluginPluginVersion]] = UNSET
    meta: Optional[Meta] = UNSET


class ListPluginVersionResponseDict(TypedDict):
    plugin_versions: NotRequired[list[FlexV1PluginPluginVersion | FlexV1PluginPluginVersionDict]]
    meta: NotRequired[Meta | MetaDict]
