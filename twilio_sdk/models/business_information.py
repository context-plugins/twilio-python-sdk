from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BusinessInformation(SdkBaseModel):
    """Business information associated with the application."""

    customer_facing_profile: str
    """The Compliance Profile SID for the customer-facing business profile."""


class BusinessInformationDict(TypedDict):
    customer_facing_profile: str
