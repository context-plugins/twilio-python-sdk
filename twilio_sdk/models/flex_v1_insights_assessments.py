from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InsightsAssessments(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    assessment_sid: OptionalNullable[str] = UNSET
    """The SID of the assessment"""

    offset: OptionalNullable[str] = UNSET
    """Offset of the conversation"""

    report: OptionalNullable[bool] = UNSET
    """The flag indicating if this assessment is part of report"""

    weight: OptionalNullable[str] = UNSET
    """The weightage given to this comment"""

    agent_id: OptionalNullable[str] = UNSET
    """The id of the Agent"""

    segment_id: OptionalNullable[str] = UNSET
    """Segment Id of conversation"""

    user_name: OptionalNullable[str] = UNSET
    """The name of the user."""

    user_email: OptionalNullable[str] = UNSET
    """The email id of the user."""

    answer_text: OptionalNullable[str] = UNSET
    """The answer text selected by user"""

    answer_id: OptionalNullable[str] = UNSET
    """The id of the answer selected by user"""

    assessment: OptionalNullable[Any] = UNSET
    """Assessment Details associated with an assessment"""

    timestamp: OptionalNullable[str] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InsightsAssessmentsDict(TypedDict):
    account_sid: NotRequired[str | None]
    assessment_sid: NotRequired[str | None]
    offset: NotRequired[str | None]
    report: NotRequired[bool | None]
    weight: NotRequired[str | None]
    agent_id: NotRequired[str | None]
    segment_id: NotRequired[str | None]
    user_name: NotRequired[str | None]
    user_email: NotRequired[str | None]
    answer_text: NotRequired[str | None]
    answer_id: NotRequired[str | None]
    assessment: NotRequired[Any | None]
    timestamp: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
