from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.supporting_document_enum_status import SupportingDocumentEnumStatusOrStr


class NumbersV2RegulatoryComplianceSupportingDocument(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string created by Twilio to identify the Supporting Document resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Document resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    mime_type: OptionalNullable[str] = UNSET
    """The image type uploaded in the Supporting Document container."""

    status: Optional[SupportingDocumentEnumStatusOrStr] = UNSET
    """The verification status of the Supporting Document resource."""

    failure_reason: OptionalNullable[str] = UNSET
    """The failure reason of the Supporting Document Resource."""

    errors: Optional[list[Any | None]] = UNSET
    """A list of errors that occurred during the registering RC Bundle"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the Supporting Document."""

    attributes: OptionalNullable[Any] = UNSET
    """The set of parameters that are the attributes of the Supporting Documents resource which are listed in the
    Supporting Document Types."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Supporting Document resource."""


class NumbersV2RegulatoryComplianceSupportingDocumentDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    mime_type: NotRequired[str | None]
    status: NotRequired[SupportingDocumentEnumStatusOrStr]
    failure_reason: NotRequired[str | None]
    errors: NotRequired[list[Any | None]]
    type_: NotRequired[str | None]
    attributes: NotRequired[Any | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
