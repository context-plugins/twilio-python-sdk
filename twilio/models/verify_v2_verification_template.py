from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class VerifyV2VerificationTemplate(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies a Verification Template."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    friendly_name: OptionalNullable[str] = UNSET
    """A descriptive string that you create to describe a Template. It can be up to 32 characters long."""

    channels: Optional[list[str | None]] = UNSET
    """A list of channels that support the Template. Can include: sms, voice."""

    translations: OptionalNullable[Any] = UNSET
    """An object that contains the different translations of the template. Every translation is identified by the
    language short name and contains its respective information as the approval status, text and created/modified
    date."""


class VerifyV2VerificationTemplateDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    channels: NotRequired[list[str | None]]
    translations: NotRequired[Any | None]
