from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InsightsQuestionnairesCategory(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Insights resource
    and owns this resource."""

    category_sid: OptionalNullable[str] = UNSET
    """The SID of the category"""

    name: OptionalNullable[str] = UNSET
    """The name of this category."""

    url: OptionalNullable[str] = UNSET


class FlexV1InsightsQuestionnairesCategoryDict(TypedDict):
    account_sid: NotRequired[str | None]
    category_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    url: NotRequired[str | None]
