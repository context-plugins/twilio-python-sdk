from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.access_token_enum_factor_types import AccessTokenEnumFactorTypesOrStr


class VerifyV2ServiceAccessToken(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this Access Token."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    service_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Verify Service."""

    entity_identity: OptionalNullable[str] = UNSET
    """The unique external identifier for the Entity of the Service."""

    factor_type: Optional[AccessTokenEnumFactorTypesOrStr] = UNSET
    """The Type of the Factor. Currently only ``push`` is supported."""

    factor_friendly_name: OptionalNullable[str] = UNSET
    """A human readable description of this factor, up to 64 characters. For a push factor, this can be the device's
    name."""

    token: OptionalNullable[str] = UNSET
    """The access token generated for enrollment, this is an encrypted json web token."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""

    ttl: Optional[int] = UNSET
    """How long, in seconds, the access token is valid. Max: 5 minutes"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this access token was created, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""


class VerifyV2ServiceAccessTokenDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    entity_identity: NotRequired[str | None]
    factor_type: NotRequired[AccessTokenEnumFactorTypesOrStr]
    factor_friendly_name: NotRequired[str | None]
    token: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    ttl: NotRequired[int]
    date_created: NotRequired[RFC3339DateTime | None]
