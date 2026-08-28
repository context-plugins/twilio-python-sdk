from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.authenticator_attachment1 import AuthenticatorAttachment1OrStr
from .enums.discoverable_credentials import DiscoverableCredentialsOrStr
from .enums.user_verification import UserVerificationOrStr
from .relying_party import RelyingParty, RelyingPartyDict


class ConfigModel(SdkBaseModel):
    relying_party: Optional[RelyingParty] = UNSET
    """Contains the information of the party requesting the user for authentication"""

    authenticator_attachment: Optional[AuthenticatorAttachment1OrStr] = UNSET
    discoverable_credentials: Optional[DiscoverableCredentialsOrStr] = UNSET
    user_verification: Optional[UserVerificationOrStr] = UNSET


class ConfigModelDict(TypedDict):
    relying_party: NotRequired[RelyingParty | RelyingPartyDict]
    authenticator_attachment: NotRequired[AuthenticatorAttachment1OrStr]
    discoverable_credentials: NotRequired[DiscoverableCredentialsOrStr]
    user_verification: NotRequired[UserVerificationOrStr]
