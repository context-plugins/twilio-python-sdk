from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.evaluation_enum_status import EvaluationEnumStatusOrStr


class NumbersV2RegulatoryComplianceBundleEvaluation(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the Evaluation resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Bundle resource."""

    regulation_sid: OptionalNullable[str] = UNSET
    """The unique string of a regulation that is associated to the Bundle resource."""

    bundle_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Bundle resource."""

    status: Optional[EvaluationEnumStatusOrStr] = UNSET
    """The compliance status of the Evaluation resource."""

    results: Optional[list[Any | None]] = UNSET
    """The results of the Evaluation which includes the valid and invalid attributes."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    url: OptionalNullable[str] = UNSET


class NumbersV2RegulatoryComplianceBundleEvaluationDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    regulation_sid: NotRequired[str | None]
    bundle_sid: NotRequired[str | None]
    status: NotRequired[EvaluationEnumStatusOrStr]
    results: NotRequired[list[Any | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
