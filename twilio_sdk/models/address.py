from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address(SdkBaseModel):
    street: str
    """The street address, ex: 101 Spear St"""

    street_2: Optional[str] = UNSET
    """The building information, ex : 5th floor."""

    city: str
    """The city name, ex: San Francisco."""

    state: str
    """The state name, ex: CA or California. Note this should match the losing carrier’s information exactly. So if they
    spell out the entire state’s name instead of abbreviating it, please do so."""

    zip: str
    """The zip code, ex: 94105."""

    country: str
    """The country, ex: USA."""


class AddressDict(TypedDict):
    street: str
    street_2: NotRequired[str]
    city: str
    state: str
    zip: str
    country: str
