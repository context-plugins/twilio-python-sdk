from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Geography(SdkBaseModel):
    """The geographic information associated with the phone number."""

    iso_country: Optional[str] = Field(default=UNSET, alias="IsoCountry")
    region: Optional[str] = Field(default=UNSET, alias="Region")
    locality: Optional[str] = Field(default=UNSET, alias="Locality")
    postal_code: Optional[str] = Field(default=UNSET, alias="PostalCode")
    latitude: Optional[float] = Field(default=UNSET, alias="Latitude")
    longitude: Optional[float] = Field(default=UNSET, alias="Longitude")
    lata: Optional[str] = Field(default=UNSET, alias="Lata")
    rate_center: Optional[str] = Field(default=UNSET, alias="RateCenter")


class GeographyDict(TypedDict):
    iso_country: NotRequired[str]
    region: NotRequired[str]
    locality: NotRequired[str]
    postal_code: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    lata: NotRequired[str]
    rate_center: NotRequired[str]
