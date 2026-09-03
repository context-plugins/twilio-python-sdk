from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Capabilities(SdkBaseModel):
    """The set of Boolean properties that indicate whether a phone number can receive calls or messages. Capabilities
    are: ``Voice``, ``SMS``, and ``MMS`` and each capability can be: ``true`` or ``false``., A mapping of capabilities
    this hosted phone number will have enabled on Twilio's platform., Set of booleans describing the capabilities hosted
    on Twilio's platform. SMS is currently only supported., The capabilities of the phone number."""

    mms: Optional[bool] = UNSET
    sms: Optional[bool] = UNSET
    voice: Optional[bool] = UNSET
    fax: Optional[bool] = UNSET


class CapabilitiesDict(TypedDict):
    mms: NotRequired[bool]
    sms: NotRequired[bool]
    voice: NotRequired[bool]
    fax: NotRequired[bool]
