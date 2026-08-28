from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Configuration3(SdkBaseModel):
    """Conversation configuration settings."""

    intelligence_configuration_ids: Optional[list[str]] = Field(default=UNSET, alias="intelligenceConfigurationIds")
    """A list of Conversational Intelligence configuration IDs."""


class Configuration3Dict(TypedDict):
    intelligence_configuration_ids: NotRequired[list[str]]
