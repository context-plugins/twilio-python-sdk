from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallType(SdkBaseModel):
    """Number of calls made in each type. ``carrier``, ``sip``, ``trunking``, ``client``, ``whatsapp``"""

    carrier: Optional[int] = UNSET
    """Number of carrier calls"""

    sip: Optional[int] = UNSET
    """Number of SIP calls"""

    trunking: Optional[int] = UNSET
    """Number of trunking calls"""

    client: Optional[int] = UNSET
    """Number of client calls"""

    whatsapp: Optional[int] = UNSET
    """Number of WhatsApp Business calls"""


class CallTypeDict(TypedDict):
    carrier: NotRequired[int]
    sip: NotRequired[int]
    trunking: NotRequired[int]
    client: NotRequired[int]
    whatsapp: NotRequired[int]
