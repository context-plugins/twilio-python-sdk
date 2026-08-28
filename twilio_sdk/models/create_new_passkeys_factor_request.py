from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .config_model import ConfigModel, ConfigModelDict


class CreateNewPasskeysFactorRequest(SdkBaseModel):
    friendly_name: str
    identity: str
    config: Optional[ConfigModel] = UNSET


class CreateNewPasskeysFactorRequestDict(TypedDict):
    friendly_name: str
    identity: str
    config: NotRequired[ConfigModel | ConfigModelDict]
