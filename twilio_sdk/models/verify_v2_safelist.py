from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class VerifyV2Safelist(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the SafeList resource."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number in SafeList."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the SafeList resource."""


class VerifyV2SafelistDict(TypedDict):
    sid: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
