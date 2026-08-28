from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v1_signing_request_configuration import (
    NumbersV1SigningRequestConfiguration,
    NumbersV1SigningRequestConfigurationDict,
)


class ListSigningRequestConfigurationResponse(SdkBaseModel):
    configurations: Optional[list[NumbersV1SigningRequestConfiguration]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSigningRequestConfigurationResponseDict(TypedDict):
    configurations: NotRequired[list[NumbersV1SigningRequestConfiguration | NumbersV1SigningRequestConfigurationDict]]
    meta: NotRequired[Meta | MetaDict]
