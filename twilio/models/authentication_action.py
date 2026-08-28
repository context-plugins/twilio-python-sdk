from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.authentication_action_type import AuthenticationActionTypeOrStr


class AuthenticationAction(SdkBaseModel):
    type_: AuthenticationActionTypeOrStr = Field(alias="type")
    copy_code_text: str


class AuthenticationActionDict(TypedDict):
    type_: AuthenticationActionTypeOrStr
    copy_code_text: str
