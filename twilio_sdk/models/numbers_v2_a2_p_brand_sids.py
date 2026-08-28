from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class NumbersV2A2PBrandSids(SdkBaseModel):
    brand_registration_sid: OptionalNullable[str] = Field(default=UNSET, alias="brandRegistrationSid")
    """Sid associated with campaign's brand"""

    external_brand_id: OptionalNullable[str] = Field(default=UNSET, alias="externalBrandId")
    """The external brand identifier (e.g., TCR Brand ID)"""


class NumbersV2A2PBrandSidsDict(TypedDict):
    brand_registration_sid: NotRequired[str | None]
    external_brand_id: NotRequired[str | None]
