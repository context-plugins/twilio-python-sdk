from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .language_properties import LanguageProperties, LanguagePropertiesDict


class LocaleResponse(SdkBaseModel):
    languages: list[LanguageProperties]
    """List of supported languages for opt-out configurations"""


class LocaleResponseDict(TypedDict):
    languages: list[LanguageProperties | LanguagePropertiesDict]
