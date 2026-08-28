from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.authorization_document_enum_status import AuthorizationDocumentEnumStatusOrStr


class NumbersV2AuthorizationDocument(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this AuthorizationDocument."""

    address_sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies the Address resource that is associated with this
    AuthorizationDocument."""

    status: Optional[AuthorizationDocumentEnumStatusOrStr] = UNSET
    """Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled,
    5. failed. See the section entitled `Status Values
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
    for more information on each of these statuses."""

    email: OptionalNullable[str] = UNSET
    """Email that this AuthorizationDocument will be sent to for signing."""

    cc_emails: Optional[list[str | None]] = UNSET
    """Email recipients who will be informed when an Authorization Document has been sent and signed."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date this resource was created, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was updated, given as `GMT RFC 2822 <http://www.ietf.org/rfc/rfc2822.txt>`__
    format."""

    url: OptionalNullable[str] = UNSET
    links: OptionalNullable[Any] = UNSET


class NumbersV2AuthorizationDocumentDict(TypedDict):
    sid: NotRequired[str | None]
    address_sid: NotRequired[str | None]
    status: NotRequired[AuthorizationDocumentEnumStatusOrStr]
    email: NotRequired[str | None]
    cc_emails: NotRequired[list[str | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
