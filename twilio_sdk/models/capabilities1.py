from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Capabilities1(SdkBaseModel):
    """The set of Boolean properties that describes the SMS, MMS, Voice, and Fax capabilities of the phone number."""

    voice: Optional[bool] = Field(default=UNSET, alias="Voice")
    restricted_voice: Optional[bool] = Field(default=UNSET, alias="RestrictedVoice")
    sms: Optional[bool] = Field(default=UNSET, alias="Sms")
    restricted_sms: Optional[bool] = Field(default=UNSET, alias="RestrictedSms")
    mms: Optional[bool] = Field(default=UNSET, alias="Mms")
    restricted_mms: Optional[bool] = Field(default=UNSET, alias="RestrictedMms")
    fax: Optional[bool] = Field(default=UNSET, alias="Fax")
    restricted_fax: Optional[bool] = Field(default=UNSET, alias="RestrictedFax")
    sip: Optional[bool] = Field(default=UNSET, alias="Sip")


class Capabilities1Dict(TypedDict):
    voice: NotRequired[bool]
    restricted_voice: NotRequired[bool]
    sms: NotRequired[bool]
    restricted_sms: NotRequired[bool]
    mms: NotRequired[bool]
    restricted_mms: NotRequired[bool]
    fax: NotRequired[bool]
    restricted_fax: NotRequired[bool]
    sip: NotRequired[bool]
