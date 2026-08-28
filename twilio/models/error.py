from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error(SdkBaseModel):
    """Error details if the operation failed. Follows RFC 9457 Problem Details."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """A URI reference that identifies the problem type."""

    title: Optional[str] = UNSET
    """A short, human-readable summary of the problem type."""

    status: Optional[int] = UNSET
    """The HTTP status code for this occurrence of the problem."""

    detail: Optional[str] = UNSET
    """A human-readable explanation specific to this occurrence."""

    instance: Optional[str] = UNSET
    """A URI reference that identifies the specific occurrence of the problem."""


class ErrorDict(TypedDict):
    type_: NotRequired[str]
    title: NotRequired[str]
    status: NotRequired[int]
    detail: NotRequired[str]
    instance: NotRequired[str]
