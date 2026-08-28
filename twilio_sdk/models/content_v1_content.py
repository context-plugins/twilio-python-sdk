from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ContentV1Content(SdkBaseModel):
    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Content resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/usage/api/account>`__ that created Content resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """A string name used to describe the Content resource. Not visible to the end recipient."""

    language: OptionalNullable[str] = UNSET
    """Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in."""

    variables: OptionalNullable[Any] = UNSET
    """Defines the default placeholder values for variables included in the Content resource. e.g. {"1":
    "Customer_Name"}."""

    types: OptionalNullable[Any] = UNSET
    """The `Content types <https://www.twilio.com/docs/content-api/content-types-overview>`__ (e.g. twilio/text) for
    this Content resource."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the resource, relative to ``https://content.twilio.com``."""

    links: OptionalNullable[Any] = UNSET
    """A list of links related to the Content resource, such as approval_fetch and approval_create"""


class ContentV1ContentDict(TypedDict):
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    language: NotRequired[str | None]
    variables: NotRequired[Any | None]
    types: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
