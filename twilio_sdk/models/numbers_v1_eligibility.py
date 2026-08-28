from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NumbersV1Eligibility(SdkBaseModel):
    results: Optional[list[Any | None]] = UNSET
    """The result set that contains the eligibility check response for the requested number, each result has at least
    the following attributes: phone_number: The requested phone number ,hosting_account_sid: The account sid where the
    phone number will be hosted, date_last_checked: Datetime (ISO 8601) when the PN was last checked for eligibility,
    country: Phone number’s country, eligibility_status: Indicates the eligibility status of the PN
    (Eligible/Ineligible), eligibility_sub_status: Indicates the sub status of the eligibility , ineligibility_reason:
    Reason for number's ineligibility (if applicable), next_step: Suggested next step in the hosting process based on
    the eligibility status."""


class NumbersV1EligibilityDict(TypedDict):
    results: NotRequired[list[Any | None]]
