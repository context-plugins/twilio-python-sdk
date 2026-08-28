from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InsightsSettingsAnswersets(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Insights resource
    and owns this resource."""

    answer_sets: OptionalNullable[Any] = UNSET
    """The lis of answer sets"""

    answer_set_categories: OptionalNullable[Any] = UNSET
    """The list of answer set categories"""

    not_applicable: OptionalNullable[Any] = UNSET
    """The details for not applicable answer set"""

    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InsightsSettingsAnswersetsDict(TypedDict):
    account_sid: NotRequired[str | None]
    answer_sets: NotRequired[Any | None]
    answer_set_categories: NotRequired[Any | None]
    not_applicable: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
