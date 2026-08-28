from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ComplianceKeywords(SdkBaseModel):
    """Compliance keywords for the application."""

    help: Optional[str] = UNSET
    stop: Optional[str] = UNSET
    info: Optional[str] = UNSET
    aide: Optional[str] = UNSET
    arret: Optional[str] = UNSET
    opt_out_filtering: Optional[bool] = UNSET


class ComplianceKeywordsDict(TypedDict):
    help: NotRequired[str]
    stop: NotRequired[str]
    info: NotRequired[str]
    aide: NotRequired[str]
    arret: NotRequired[str]
    opt_out_filtering: NotRequired[bool]
