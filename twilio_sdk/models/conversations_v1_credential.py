from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.credential_enum_push_type import CredentialEnumPushTypeOrStr


class ConversationsV1Credential(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this
    credential."""

    friendly_name: OptionalNullable[str] = UNSET
    """The human-readable name of this credential, limited to 64 characters. Optional."""

    type_: Optional[CredentialEnumPushTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``."""

    sandbox: OptionalNullable[str] = UNSET
    """[APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs or ``false``
    to send to production."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated."""

    url: OptionalNullable[AnyUrl] = UNSET
    """An absolute API resource URL for this credential."""


class ConversationsV1CredentialDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    type_: NotRequired[CredentialEnumPushTypeOrStr]
    sandbox: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
