from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthenticatorAttachment(str, Enum):
    """A string that indicates the mechanism by which the WebAuthn implementation is attached to the authenticator at
    the time the associated ``navigator.credentials.create()`` or ``navigator.credentials.get()`` call completes."""

    PLATFORM = "platform"
    CROSS_PLATFORM = "cross-platform"

    __str__ = str.__str__


AuthenticatorAttachmentOrStr: TypeAlias = Annotated[
    AuthenticatorAttachment | str, open_enum_validator(AuthenticatorAttachment)
]
