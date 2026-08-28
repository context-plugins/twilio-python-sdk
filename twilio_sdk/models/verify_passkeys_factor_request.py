from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.authenticator_attachment import AuthenticatorAttachmentOrStr
from .enums.type import TypeOrStr
from .response import Response, ResponseDict


class VerifyPasskeysFactorRequest(SdkBaseModel):
    id: Optional[str] = UNSET
    """A `base64url <https://base64.guru/standards/base64url>`__ encoded representation of ``rawId``."""

    raw_id: Optional[str] = Field(default=UNSET, alias="rawId")
    """The globally unique identifier for this ``PublicKeyCredential``."""

    authenticator_attachment: Optional[AuthenticatorAttachmentOrStr] = Field(
        default=UNSET, alias="authenticatorAttachment"
    )
    """A string that indicates the mechanism by which the WebAuthn implementation is attached to the authenticator at
    the time the associated ``navigator.credentials.create()`` or ``navigator.credentials.get()`` call completes."""

    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    """The valid credential types supported by the API. The values of this enumeration are used for versioning the
    ``AuthenticatorAssertion`` and ``AuthenticatorAttestation`` structures according to the type of the
    authenticator."""

    response: Response
    """The result of a WebAuthn credential registration via ``navigator.credentials.create()``, as specified in
    `AuthenticatorAttestationResponse
    <https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAttestationResponse>`__."""


class VerifyPasskeysFactorRequestDict(TypedDict):
    id: NotRequired[str]
    raw_id: NotRequired[str]
    authenticator_attachment: NotRequired[AuthenticatorAttachmentOrStr]
    type_: NotRequired[TypeOrStr]
    response: Response | ResponseDict
