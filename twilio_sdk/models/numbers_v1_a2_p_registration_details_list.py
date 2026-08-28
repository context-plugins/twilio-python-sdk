from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .numbers_v1_a2_p_registration_details import NumbersV1A2PRegistrationDetails, NumbersV1A2PRegistrationDetailsDict


class NumbersV1A2PRegistrationDetailsList(SdkBaseModel):
    data: list[NumbersV1A2PRegistrationDetails]


class NumbersV1A2PRegistrationDetailsListDict(TypedDict):
    data: list[NumbersV1A2PRegistrationDetails | NumbersV1A2PRegistrationDetailsDict]
