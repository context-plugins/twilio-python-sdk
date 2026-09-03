from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Capabilities7(SdkBaseModel):
    """The set of Boolean properties that indicate whether a phone number can receive calls or messages. Capabilities
    are ``Voice``, ``SMS``, and ``MMS`` and each capability can be: ``true`` or ``false``."""

    mms: Optional[bool] = UNSET
    sms: Optional[bool] = UNSET
    voice: Optional[bool] = UNSET
    fax: Optional[bool] = UNSET


class Capabilities7Dict(TypedDict):
    mms: NotRequired[bool]
    sms: NotRequired[bool]
    voice: NotRequired[bool]
    fax: NotRequired[bool]
