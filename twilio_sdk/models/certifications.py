from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Certifications(SdkBaseModel):
    """The certifications required for the phone number."""

    resident: Optional[bool] = Field(default=UNSET, alias="Resident")
    non_resident: Optional[bool] = Field(default=UNSET, alias="Non-Resident")


class CertificationsDict(TypedDict):
    resident: NotRequired[bool]
    non_resident: NotRequired[bool]
