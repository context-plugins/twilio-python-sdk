from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_plugin import FlexV1Plugin, FlexV1PluginDict
from .meta import Meta, MetaDict


class ListPluginResponse(SdkBaseModel):
    plugins: Optional[list[FlexV1Plugin]] = UNSET
    meta: Optional[Meta] = UNSET


class ListPluginResponseDict(TypedDict):
    plugins: NotRequired[list[FlexV1Plugin | FlexV1PluginDict]]
    meta: NotRequired[Meta | MetaDict]
