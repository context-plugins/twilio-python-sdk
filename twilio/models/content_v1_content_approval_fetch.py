from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ContentV1ContentApprovalFetch(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Content resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/usage/api/account>`__ that created Content resource."""

    whatsapp: OptionalNullable[Any] = UNSET
    """Contains the whatsapp approval information for the Content resource, with fields such as approval status,
    rejection reason, and category, amongst others."""

    url: OptionalNullable[str] = UNSET
    """The URL of the resource, relative to ``https://content.twilio.com``."""


class ContentV1ContentApprovalFetchDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    whatsapp: NotRequired[Any | None]
    url: NotRequired[str | None]
