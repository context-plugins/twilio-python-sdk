from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .numbers_v1_a2_p_registration_details import NumbersV1A2PRegistrationDetails, NumbersV1A2PRegistrationDetailsDict


class NumbersV1A2PRegistrationDetailsCampaignList(SdkBaseModel):
    data: list[NumbersV1A2PRegistrationDetails]
    """List of A2P registration details for numbers in the campaign"""

    next_token: OptionalNullable[str] = Field(default=UNSET, alias="nextToken")
    """Token for pagination to retrieve the next page of results"""


class NumbersV1A2PRegistrationDetailsCampaignListDict(TypedDict):
    data: list[NumbersV1A2PRegistrationDetails | NumbersV1A2PRegistrationDetailsDict]
    next_token: NotRequired[str | None]
