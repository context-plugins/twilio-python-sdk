from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class NumbersV1BulkEligibility(SdkBaseModel):
    request_id: OptionalNullable[str] = UNSET
    """The SID of the bulk eligibility check that you want to know about."""

    url: OptionalNullable[AnyUrl] = UNSET
    """This is the url of the request that you're trying to reach out to locate the resource."""

    results: Optional[list[Any | None]] = UNSET
    """The result set that contains the eligibility check response for each requested number, each result has at least
    the following attributes: phone_number: The requested phone number ,hosting_account_sid: The account sid where the
    phone number will be hosted, country: Phone number’s country, eligibility_status: Indicates the eligibility status
    of the PN (Eligible/Ineligible), eligibility_sub_status: Indicates the sub status of the eligibility ,
    ineligibility_reason: Reason for number's ineligibility (if applicable), next_step: Suggested next step in the
    hosting process based on the eligibility status."""

    friendly_name: OptionalNullable[str] = UNSET
    """This is the string that you assigned as a friendly name for describing the eligibility check request."""

    status: OptionalNullable[str] = UNSET
    """This is the status of the bulk eligibility check request. (Example: COMPLETE, IN_PROGRESS)"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    date_completed: OptionalNullable[RFC3339DateTime] = UNSET


class NumbersV1BulkEligibilityDict(TypedDict):
    request_id: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    results: NotRequired[list[Any | None]]
    friendly_name: NotRequired[str | None]
    status: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_completed: NotRequired[RFC3339DateTime | None]
