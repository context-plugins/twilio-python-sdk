from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_plugin_release import FlexV1PluginRelease, FlexV1PluginReleaseDict
from .meta import Meta, MetaDict


class ListPluginReleaseResponse(SdkBaseModel):
    releases: Optional[list[FlexV1PluginRelease]] = UNSET
    meta: Optional[Meta] = UNSET


class ListPluginReleaseResponseDict(TypedDict):
    releases: NotRequired[list[FlexV1PluginRelease | FlexV1PluginReleaseDict]]
    meta: NotRequired[Meta | MetaDict]
