from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.authenticator_attachment2 import AuthenticatorAttachment2OrStr
from .enums.type1 import Type1OrStr
from .response1 import Response1, Response1Dict


class ApprovePasskeysChallengeRequest(SdkBaseModel):
    id: str
    """A `base64url <https://base64.guru/standards/base64url>`__ encoded representation of ``rawId``."""

    raw_id: str = Field(alias="rawId")
    """The globally unique identifier for this ``PublicKeyCredential``."""

    authenticator_attachment: AuthenticatorAttachment2OrStr = Field(alias="authenticatorAttachment")
    """A string that indicates the mechanism by which the WebAuthn implementation is attached to the authenticator at
    the time the associated ``navigator.credentials.create()`` or ``navigator.credentials.get()`` call completes."""

    type_: Optional[Type1OrStr] = Field(default=UNSET, alias="type")
    """The valid credential types supported by the API. The values of this enumeration are used for versioning the
    ``AuthenticatorAssertion`` and ``AuthenticatorAttestation`` structures according to the type of the
    authenticator."""

    response: Response1
    """The result of a WebAuthn authentication via a ``navigator.credentials.get()`` request, as specified in
    `AuthenticatorAttestationResponse
    <https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAttestationResponse>`__."""


class ApprovePasskeysChallengeRequestDict(TypedDict):
    id: str
    raw_id: str
    authenticator_attachment: AuthenticatorAttachment2OrStr
    type_: NotRequired[Type1OrStr]
    response: Response1 | Response1Dict
