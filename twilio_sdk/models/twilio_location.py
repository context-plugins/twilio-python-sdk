from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TwilioLocation(SdkBaseModel):
    """twilio/location type contains a location pin and an optional label, which can be used to enhance delivery
    notifications or connect recipients to physical experiences you offer."""

    latitude: float
    longitude: float
    label: Optional[str] = UNSET
    id: Optional[str] = UNSET
    address: Optional[str] = UNSET


class TwilioLocationDict(TypedDict):
    latitude: float
    longitude: float
    label: NotRequired[str]
    id: NotRequired[str]
    address: NotRequired[str]
