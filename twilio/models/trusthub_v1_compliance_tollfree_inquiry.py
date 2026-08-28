from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TrusthubV1ComplianceTollfreeInquiry(SdkBaseModel):
    inquiry_id: OptionalNullable[str] = UNSET
    """The unique ID used to start an embedded compliance registration session."""

    inquiry_session_token: OptionalNullable[str] = UNSET
    """The session token used to start an embedded compliance registration session."""

    registration_id: OptionalNullable[str] = UNSET
    """The TolfreeId matching the Tollfree Profile that should be resumed or resubmitted for editing."""

    url: OptionalNullable[str] = UNSET
    """The URL of this resource."""


class TrusthubV1ComplianceTollfreeInquiryDict(TypedDict):
    inquiry_id: NotRequired[str | None]
    inquiry_session_token: NotRequired[str | None]
    registration_id: NotRequired[str | None]
    url: NotRequired[str | None]
