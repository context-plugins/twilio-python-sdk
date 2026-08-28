from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.annotation_enum_answered_by import AnnotationEnumAnsweredByOrStr
from .enums.annotation_enum_connectivity_issue import AnnotationEnumConnectivityIssueOrStr


class InsightsV1CallAnnotation(SdkBaseModel):
    call_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Call."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    answered_by: Optional[AnnotationEnumAnsweredByOrStr] = UNSET
    connectivity_issue: Optional[AnnotationEnumConnectivityIssueOrStr] = UNSET
    quality_issues: Optional[list[str | None]] = UNSET
    """Specifies if the call had any subjective quality issues. Possible values are one or more of ``no_quality_issue``,
    ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``, or ``static_noise``."""

    spam: OptionalNullable[bool] = UNSET
    """Specifies if the call was a spam call. Use this to provide feedback on whether calls placed from your account
    were marked as spam, or if inbound calls received by your account were unwanted spam. Is of type Boolean: true,
    false. Use true if the call was a spam call."""

    call_score: OptionalNullable[int] = UNSET
    """Specifies the Call Score, if available. This is of type integer. Use a range of 1-5 to indicate the call
    experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2
    : Poor, 1: Bad]."""

    comment: OptionalNullable[str] = UNSET
    """Specifies any comments pertaining to the call. Twilio does not treat this field as PII, so no PII should be
    included in comments."""

    incident: OptionalNullable[str] = UNSET
    """Incident or support ticket associated with this call. The ``incident`` property is of type string with a maximum
    character limit of 100. Twilio does not treat this field as PII, so no PII should be included in ``incident``."""

    url: OptionalNullable[AnyUrl] = UNSET


class InsightsV1CallAnnotationDict(TypedDict):
    call_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    answered_by: NotRequired[AnnotationEnumAnsweredByOrStr]
    connectivity_issue: NotRequired[AnnotationEnumConnectivityIssueOrStr]
    quality_issues: NotRequired[list[str | None]]
    spam: NotRequired[bool | None]
    call_score: NotRequired[int | None]
    comment: NotRequired[str | None]
    incident: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
