from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateShortCodeApplicationBundleInquiryRequest(SdkBaseModel):
    application_sid: str
    """The unique identifier of the Short Code Application."""


class CreateShortCodeApplicationBundleInquiryRequestDict(TypedDict):
    application_sid: str
