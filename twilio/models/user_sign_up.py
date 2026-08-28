from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sign_up_option import SignUpOptionOrStr


class UserSignUp(SdkBaseModel):
    """User sign-up configuration for the application."""

    sign_up_options: Optional[list[SignUpOptionOrStr]] = UNSET
    double_opt_in_process: Optional[bool] = UNSET
    double_opt_in_message: Optional[str] = UNSET
    sign_up_confirmation_message: Optional[str] = UNSET
    double_opt_in_response_message: Optional[str] = UNSET
    online_web_form_message: Optional[str] = UNSET
    keyword_message: Optional[str] = UNSET
    ivr_message: Optional[str] = UNSET
    other_form_message: Optional[str] = UNSET


class UserSignUpDict(TypedDict):
    sign_up_options: NotRequired[list[SignUpOptionOrStr]]
    double_opt_in_process: NotRequired[bool]
    double_opt_in_message: NotRequired[str]
    sign_up_confirmation_message: NotRequired[str]
    double_opt_in_response_message: NotRequired[str]
    online_web_form_message: NotRequired[str]
    keyword_message: NotRequired[str]
    ivr_message: NotRequired[str]
    other_form_message: NotRequired[str]
