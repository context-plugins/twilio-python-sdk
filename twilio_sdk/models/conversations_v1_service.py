from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ConversationsV1Service(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique ID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for this service."""

    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The human-readable name of this service, limited to 256 characters. Optional."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this resource was last updated."""

    url: OptionalNullable[str] = UNSET
    """An absolute API resource URL for this service."""

    links: OptionalNullable[Any] = UNSET
    """Contains absolute API resource URLs to access conversations, users, roles, bindings and configuration of this
    service."""


class ConversationsV1ServiceDict(TypedDict):
    account_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
