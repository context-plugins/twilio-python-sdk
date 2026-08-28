from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FlexV1InsightsQuestionnairesQuestion(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Insights resource
    and owns this resource."""

    question_sid: OptionalNullable[str] = UNSET
    """The SID of the question"""

    question: OptionalNullable[str] = UNSET
    """The question."""

    description: OptionalNullable[str] = UNSET
    """The description for the question."""

    category: OptionalNullable[Any] = UNSET
    """The Category for the question."""

    answer_set_id: OptionalNullable[str] = UNSET
    """The answer_set for the question."""

    allow_na: OptionalNullable[bool] = UNSET
    """The flag to enable for disable NA for answer."""

    usage: Optional[int] = UNSET
    """Integer value that tells a particular question is used by how many questionnaires"""

    answer_set: OptionalNullable[Any] = UNSET
    """Set of answers for the question"""

    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InsightsQuestionnairesQuestionDict(TypedDict):
    account_sid: NotRequired[str | None]
    question_sid: NotRequired[str | None]
    question: NotRequired[str | None]
    description: NotRequired[str | None]
    category: NotRequired[Any | None]
    answer_set_id: NotRequired[str | None]
    allow_na: NotRequired[bool | None]
    usage: NotRequired[int]
    answer_set: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
