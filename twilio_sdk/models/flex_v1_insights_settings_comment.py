from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InsightsSettingsComment(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Flex Insights resource
    and owns this resource."""

    comments: OptionalNullable[Any] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InsightsSettingsCommentDict(TypedDict):
    account_sid: NotRequired[str | None]
    comments: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
