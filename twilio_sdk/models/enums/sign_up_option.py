from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SignUpOption(str, Enum):
    ONLINE_WEB_FORM = "ONLINE_WEB_FORM"
    IVR = "IVR"
    VERBALLY = "VERBALLY"
    MOBILE_APP_OR_DIGITAL_KIOSK = "MOBILE_APP_OR_DIGITAL_KIOSK"
    PAPER_FORM = "PAPER_FORM"
    SHORTCODE_KEYWORD = "SHORTCODE_KEYWORD"
    OTHER_FORM = "OTHER_FORM"

    __str__ = str.__str__


SignUpOptionOrStr: TypeAlias = Annotated[SignUpOption | str, open_enum_validator(SignUpOption)]
