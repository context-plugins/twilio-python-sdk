from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class NumbersV1CreateEmbeddedRegistrationRequest(SdkBaseModel):
    regulation_id: str = Field(alias="regulationId")
    """The regulation for this registration."""

    regulation_version: int = Field(alias="regulationVersion")
    """The regulation version."""

    friendly_name: str = Field(alias="friendlyName")
    """Human-readable name for the registration."""

    status_notification_email: Optional[EmailStr] = Field(default=UNSET, alias="statusNotificationEmail")
    """Email address for registration status notifications."""

    status_callback_url: OptionalNullable[AnyUrl] = Field(default=UNSET, alias="statusCallbackUrl")
    """The URL of this resource."""

    comments: Optional[str] = UNSET
    """Additional comments about the registration."""

    theme_set_id: Optional[str] = Field(default=UNSET, alias="themeSetId")
    """Theme ID for the Compliance Embeddable UI."""

    data: Any
    """Registration data organized by section (alphanumericSender, business, useCase, authorizedRepresentative, officer,
    businessAddress)."""


class NumbersV1CreateEmbeddedRegistrationRequestDict(TypedDict):
    regulation_id: str
    regulation_version: int
    friendly_name: str
    status_notification_email: NotRequired[EmailStr]
    status_callback_url: NotRequired[AnyUrl | None]
    comments: NotRequired[str]
    theme_set_id: NotRequired[str]
    data: Any
