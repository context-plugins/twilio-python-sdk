from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TrusthubV1ComplianceInquiry(SdkBaseModel):
    inquiry_id: OptionalNullable[str] = UNSET
    """The unique ID used to start an embedded compliance registration session."""

    inquiry_session_token: OptionalNullable[str] = UNSET
    """The session token used to start an embedded compliance registration session."""

    customer_id: OptionalNullable[str] = UNSET
    """The CustomerID matching the Customer Profile that should be resumed or resubmitted for editing."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""


class TrusthubV1ComplianceInquiryDict(TypedDict):
    inquiry_id: NotRequired[str | None]
    inquiry_session_token: NotRequired[str | None]
    customer_id: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
