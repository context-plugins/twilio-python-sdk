from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MessagingV1DomainDnsValidation(SdkBaseModel):
    domain_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Domain resource."""

    is_valid: OptionalNullable[bool] = UNSET
    reason: OptionalNullable[str] = UNSET
    url: OptionalNullable[str] = UNSET


class MessagingV1DomainDnsValidationDict(TypedDict):
    domain_sid: NotRequired[str | None]
    is_valid: NotRequired[bool | None]
    reason: NotRequired[str | None]
    url: NotRequired[str | None]
