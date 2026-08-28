from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV2DomainCertV4(SdkBaseModel):
    domain_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Domain resource."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """Date that this Domain was last updated."""

    date_expires: OptionalNullable[RFC3339DateTime] = UNSET
    """Date that the private certificate associated with this domain expires. You will need to update the certificate
    before that date to ensure your shortened links will continue to work."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """Date that this Domain was registered to the Twilio platform to create a new Domain object."""

    domain_name: OptionalNullable[AnyUrl] = UNSET
    """Full url path for this domain."""

    certificate_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify this Certificate resource."""

    managed: OptionalNullable[bool] = UNSET
    """Boolean field that indicates whether the certificate is managed by Twilio or uploaded by the customer."""

    requesting: OptionalNullable[bool] = UNSET
    """Boolean field that indicates whether a Twilio managed cert request is in progress or completed. True indicates a
    request is in progress and false indicates the request has completed or not requested yet."""

    url: OptionalNullable[AnyUrl] = UNSET
    cert_in_validation: OptionalNullable[Any] = UNSET
    """Optional JSON field describing the status and upload date of a new certificate in the process of validation"""


class MessagingV2DomainCertV4Dict(TypedDict):
    domain_sid: NotRequired[str | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    date_expires: NotRequired[RFC3339DateTime | None]
    date_created: NotRequired[RFC3339DateTime | None]
    domain_name: NotRequired[AnyUrl | None]
    certificate_sid: NotRequired[str | None]
    managed: NotRequired[bool | None]
    requesting: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
    cert_in_validation: NotRequired[Any | None]
