from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Response1(SdkBaseModel):
    """The result of a WebAuthn authentication via a ``navigator.credentials.get()`` request, as specified in
    `AuthenticatorAttestationResponse
    <https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAttestationResponse>`__."""

    authenticator_data: str = Field(alias="authenticatorData")
    """The `authenticator data
    <https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API/Authenticator_data>`__ structure contains
    information from the authenticator about the processing of a credential creation or authentication request."""

    client_data_json: str = Field(alias="clientDataJSON")
    """This property contains the JSON-compatible serialization of the data passed from the browser to the authenticator
    in order to generate this credential."""

    signature: str
    """An assertion signature over ``authenticatorData`` and ``clientDataJSON``. The assertion signature is created with
    the private key of the key pair that was created during the originating ``navigator.credentials.create()`` call and
    verified using the public key of that same key pair."""

    user_handle: Optional[str] = Field(default=UNSET, alias="userHandle")
    """The user handle stored in the authenticator, specified as ``user.id`` in the options passed to the originating
    ``navigator.credentials.create()`` call. This property should contain a base64url-encoded entity SID."""


class Response1Dict(TypedDict):
    authenticator_data: str
    client_data_json: str
    signature: str
    user_handle: NotRequired[str]
