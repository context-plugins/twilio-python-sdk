from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1RequestManagedCert(SdkBaseModel):
    domain_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Domain resource."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """Date that this Domain was last updated."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """Date that this Domain was registered to the Twilio platform to create a new Domain object."""

    date_expires: OptionalNullable[RFC3339DateTime] = UNSET
    """Date that the private certificate associated with this domain expires. This is the expiration date of your
    existing cert."""

    domain_name: OptionalNullable[AnyUrl] = UNSET
    """Full url path for this domain."""

    certificate_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify this Certificate resource."""

    url: OptionalNullable[AnyUrl] = UNSET
    managed: OptionalNullable[bool] = UNSET
    """A boolean flag indicating if the certificate is managed by Twilio."""

    requesting: OptionalNullable[bool] = UNSET
    """A boolean flag indicating if a managed certificate needs to be fulfilled by Twilio."""


class MessagingV1RequestManagedCertDict(TypedDict):
    domain_sid: NotRequired[str | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_expires: NotRequired[RFC3339DateTime | None]
    domain_name: NotRequired[AnyUrl | None]
    certificate_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    managed: NotRequired[bool | None]
    requesting: NotRequired[bool | None]
