from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MessagingV1BrandRegistrationsBrandRegistrationOtp(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Brand Registration
    resource."""

    brand_registration_sid: OptionalNullable[str] = UNSET
    """The unique string to identify Brand Registration of Sole Proprietor Brand"""


class MessagingV1BrandRegistrationsBrandRegistrationOtpDict(TypedDict):
    account_sid: NotRequired[str | None]
    brand_registration_sid: NotRequired[str | None]
