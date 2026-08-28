from __future__ import annotations

from typing import Any

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .numbers_v1_embedded_session import NumbersV1EmbeddedSession, NumbersV1EmbeddedSessionDict


class NumbersV1CreateEmbeddedRegistrationResponse(SdkBaseModel):
    id: str
    """Registration identifier (BU-prefixed)."""

    regulation_id: str = Field(alias="regulationId")
    """The regulation ID for this registration."""

    regulation_version: int = Field(alias="regulationVersion")
    """The regulation version."""

    friendly_name: str = Field(alias="friendlyName")
    """The friendly name provided in the request."""

    status: str
    """Registration status. Always DRAFT on creation."""

    status_notification_email: OptionalNullable[EmailStr] = Field(default=UNSET, alias="statusNotificationEmail")
    """Email address for status notifications."""

    status_callback_url: OptionalNullable[str] = Field(default=UNSET, alias="statusCallbackUrl")
    """Callback URL for status webhooks."""

    comments: OptionalNullable[str] = UNSET
    """Additional comments."""

    embedded_session: NumbersV1EmbeddedSession = Field(alias="embeddedSession")
    data: Any
    """Registration data echoed from the request."""

    date_created: RFC3339DateTime = Field(alias="dateCreated")
    """Timestamp of creation."""

    date_updated: RFC3339DateTime = Field(alias="dateUpdated")
    """Timestamp of last update."""


class NumbersV1CreateEmbeddedRegistrationResponseDict(TypedDict):
    id: str
    regulation_id: str
    regulation_version: int
    friendly_name: str
    status: str
    status_notification_email: NotRequired[EmailStr | None]
    status_callback_url: NotRequired[str | None]
    comments: NotRequired[str | None]
    embedded_session: NumbersV1EmbeddedSession | NumbersV1EmbeddedSessionDict
    data: Any
    date_created: RFC3339DateTime
    date_updated: RFC3339DateTime
