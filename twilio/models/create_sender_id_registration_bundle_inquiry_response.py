from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateSenderIdRegistrationBundleInquiryResponse(SdkBaseModel):
    inquiry_id: Optional[str] = UNSET
    """The unique identifier of the inquiry."""

    inquiry_session_token: Optional[str] = UNSET
    """The session token for the inquiry."""

    application_sid: Optional[str] = UNSET
    """The unique identifier of the Sender ID Registration Application."""

    bundle_sid: Optional[str] = UNSET
    """The Bundle SID associated with the inquiry."""


class CreateSenderIdRegistrationBundleInquiryResponseDict(TypedDict):
    inquiry_id: NotRequired[str]
    inquiry_session_token: NotRequired[str]
    application_sid: NotRequired[str]
    bundle_sid: NotRequired[str]
