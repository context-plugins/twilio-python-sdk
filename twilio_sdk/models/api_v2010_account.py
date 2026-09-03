from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.account_enum_status import AccountEnumStatusOrStr
from .enums.account_enum_type import AccountEnumTypeOrStr


class ApiV2010Account(SdkBaseModel):
    auth_token: OptionalNullable[str] = UNSET
    """The authorization token for this account. This token should be kept a secret, so no sharing."""

    date_created: OptionalNullable[str] = UNSET
    """The date that this account was created, in GMT in RFC 2822 format"""

    date_updated: OptionalNullable[str] = UNSET
    """The date that this account was last updated, in GMT in RFC 2822 format."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human readable description of this account, up to 64 characters long. By default the FriendlyName is your email
    address."""

    owner_account_sid: OptionalNullable[str] = UNSET
    """The unique 34 character id that represents the parent of this account. The OwnerAccountSid of a parent account is
    it's own sid."""

    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    status: Optional[AccountEnumStatusOrStr] = UNSET
    """The status of this account. Usually ``active``, but can be ``suspended`` or ``closed``."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A Map of various subresources available for the given Account Instance"""

    type_: Optional[AccountEnumTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of this account. Either ``Trial`` or ``Full`` if it's been upgraded"""

    uri: OptionalNullable[str] = UNSET
    """The URI for this resource, relative to ``https://api.twilio.com``"""


class ApiV2010AccountDict(TypedDict):
    auth_token: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    owner_account_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    status: NotRequired[AccountEnumStatusOrStr]
    subresource_uris: NotRequired[Any | None]
    type_: NotRequired[AccountEnumTypeOrStr]
    uri: NotRequired[str | None]
