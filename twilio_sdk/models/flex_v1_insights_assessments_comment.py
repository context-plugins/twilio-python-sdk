from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InsightsAssessmentsComment(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Insights resource
    and owns this resource."""

    assessment_sid: OptionalNullable[str] = UNSET
    """The SID of the assessment."""

    comment: OptionalNullable[Any] = UNSET
    """The comment added for assessment."""

    offset: OptionalNullable[str] = UNSET
    """The offset"""

    report: OptionalNullable[bool] = UNSET
    """The flag indicating if this assessment is part of report"""

    weight: OptionalNullable[str] = UNSET
    """The weightage given to this comment"""

    agent_id: OptionalNullable[str] = UNSET
    """The id of the agent."""

    segment_id: OptionalNullable[str] = UNSET
    """The id of the segment."""

    user_name: OptionalNullable[str] = UNSET
    """The name of the user."""

    user_email: OptionalNullable[str] = UNSET
    """The email id of the user."""

    timestamp: OptionalNullable[str] = UNSET
    """The timestamp when the record is inserted"""

    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InsightsAssessmentsCommentDict(TypedDict):
    account_sid: NotRequired[str | None]
    assessment_sid: NotRequired[str | None]
    comment: NotRequired[Any | None]
    offset: NotRequired[str | None]
    report: NotRequired[bool | None]
    weight: NotRequired[str | None]
    agent_id: NotRequired[str | None]
    segment_id: NotRequired[str | None]
    user_name: NotRequired[str | None]
    user_email: NotRequired[str | None]
    timestamp: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
