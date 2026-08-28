from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .authentication_action import AuthenticationAction, AuthenticationActionDict


class WhatsappAuthentication(SdkBaseModel):
    """whatsApp/authentication templates let companies deliver WA approved one-time-password button."""

    add_security_recommendation: Optional[bool] = UNSET
    code_expiration_minutes: Optional[float] = UNSET
    actions: list[AuthenticationAction]


class WhatsappAuthenticationDict(TypedDict):
    add_security_recommendation: NotRequired[bool]
    code_expiration_minutes: NotRequired[float]
    actions: list[AuthenticationAction | AuthenticationActionDict]
