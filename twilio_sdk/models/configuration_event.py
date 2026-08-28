from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .languages import Languages, LanguagesDict


class ConfigurationEvent(SdkBaseModel):
    configurations: Optional[dict[str, str]] = UNSET
    """Key-value pairs for configuration settings."""

    languages: Optional[dict[str, Languages]] = UNSET
    """Key-value pairs for language configurations."""


class ConfigurationEventDict(TypedDict):
    configurations: NotRequired[dict[str, str]]
    languages: NotRequired[dict[str, Languages | LanguagesDict]]
