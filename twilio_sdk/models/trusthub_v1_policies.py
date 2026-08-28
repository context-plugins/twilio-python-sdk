from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TrusthubV1Policies(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the Policy resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human-readable description that is assigned to describe the Policy resource. Examples can include Primary
    Customer profile policy"""

    requirements: OptionalNullable[Any] = UNSET
    """The SID of an object that holds the policy information"""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Policy resource."""


class TrusthubV1PoliciesDict(TypedDict):
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    requirements: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
