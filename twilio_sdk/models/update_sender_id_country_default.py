from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateSenderIdCountryDefault(SdkBaseModel):
    default: Optional[bool] = UNSET
    """Default Sender Id to use for replacement"""


class UpdateSenderIdCountryDefaultDict(TypedDict):
    default: NotRequired[bool]
