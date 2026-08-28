from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .business_information import BusinessInformation, BusinessInformationDict
from .setup import Setup, SetupDict


class CreateShortCodeApplicationRequest(SdkBaseModel):
    friendly_name: str
    """The friendly name for the short code application."""

    iso_country: str
    """The ISO country code."""

    business_information: BusinessInformation
    """Business information associated with the application."""

    setup: Setup


class CreateShortCodeApplicationRequestDict(TypedDict):
    friendly_name: str
    iso_country: str
    business_information: BusinessInformation | BusinessInformationDict
    setup: Setup | SetupDict
