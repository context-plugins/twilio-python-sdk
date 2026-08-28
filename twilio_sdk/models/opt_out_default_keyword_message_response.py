from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .default_keyword import DefaultKeyword, DefaultKeywordDict


class OptOutDefaultKeywordMessageResponse(SdkBaseModel):
    default_keywords: Optional[list[DefaultKeyword]] = Field(default=UNSET, alias="defaultKeywords")


class OptOutDefaultKeywordMessageResponseDict(TypedDict):
    default_keywords: NotRequired[list[DefaultKeyword | DefaultKeywordDict]]
