from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.account_type import AccountTypeOrStr
from .enums.verification_method import VerificationMethodOrStr


class MessagingV2ChannelsSenderConfiguration(SdkBaseModel):
    """The configuration settings for creating a sender."""

    waba_id: OptionalNullable[str] = UNSET
    """The ID of the WhatsApp Business Account (WABA) to use for this sender."""

    verification_method: OptionalNullable[VerificationMethodOrStr] = UNSET
    """The verification method."""

    verification_code: OptionalNullable[str] = UNSET
    """The verification code."""

    voice_application_sid: OptionalNullable[str] = UNSET
    """The SID of the Twilio Voice application."""

    account_type: OptionalNullable[AccountTypeOrStr] = UNSET
    """The account type for ISV Account Type Migration. Set to 'ISV' or 'ISVSubAccount' to configure, empty string to
    clear, or omit to preserve the existing value."""


class MessagingV2ChannelsSenderConfigurationDict(TypedDict):
    waba_id: NotRequired[str | None]
    verification_method: NotRequired[VerificationMethodOrStr | None]
    verification_code: NotRequired[str | None]
    voice_application_sid: NotRequired[str | None]
    account_type: NotRequired[AccountTypeOrStr | None]
