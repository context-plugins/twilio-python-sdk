from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FlexV1InsightsQuestionnaires(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Insights resource
    and owns this resource."""

    questionnaire_sid: OptionalNullable[str] = UNSET
    """The sid of this questionnaire"""

    name: OptionalNullable[str] = UNSET
    """The name of this category."""

    description: OptionalNullable[str] = UNSET
    """The description of this questionnaire"""

    active: OptionalNullable[bool] = UNSET
    """The flag to enable or disable questionnaire"""

    questions: Optional[list[Any | None]] = UNSET
    """The list of questions with category for a questionnaire"""

    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InsightsQuestionnairesDict(TypedDict):
    account_sid: NotRequired[str | None]
    questionnaire_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    description: NotRequired[str | None]
    active: NotRequired[bool | None]
    questions: NotRequired[list[Any | None]]
    url: NotRequired[AnyUrl | None]
