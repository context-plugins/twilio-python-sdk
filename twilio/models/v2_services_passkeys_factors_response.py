from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.factor_enum_factor_statuses import FactorEnumFactorStatusesOrStr
from .enums.factor_enum_factor_types import FactorEnumFactorTypesOrStr


class V2ServicesPasskeysFactorsResponse(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this Factor."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    service_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Service."""

    entity_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Entity."""

    identity: OptionalNullable[str] = UNSET
    """Customer unique identity for the Entity owner of the Factor."""

    binding: OptionalNullable[Any] = UNSET
    """Contains the ``factor_type`` specific secret and metadata. The Binding property is ONLY returned upon Factor
    creation."""

    options: OptionalNullable[Any] = UNSET
    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this Factor was created, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this Factor was updated, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The friendly name of this Factor. This can be any string up to 64 characters, meant for humans to distinguish
    between Factors."""

    status: Optional[FactorEnumFactorStatusesOrStr] = UNSET
    """The Status of this Factor. One of ``unverified`` or ``verified``."""

    factor_type: Optional[FactorEnumFactorTypesOrStr] = UNSET
    """The Type of this Factor. Currently ``push`` and ``totp`` are supported."""

    config: OptionalNullable[Any] = UNSET
    """An object that contains configurations specific to a ``factor_type``."""

    metadata: OptionalNullable[Any] = UNSET
    """Custom metadata associated with the factor."""

    url: OptionalNullable[str] = UNSET
    """The URL of this resource."""


class V2ServicesPasskeysFactorsResponseDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    entity_sid: NotRequired[str | None]
    identity: NotRequired[str | None]
    binding: NotRequired[Any | None]
    options: NotRequired[Any | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    friendly_name: NotRequired[str | None]
    status: NotRequired[FactorEnumFactorStatusesOrStr]
    factor_type: NotRequired[FactorEnumFactorTypesOrStr]
    config: NotRequired[Any | None]
    metadata: NotRequired[Any | None]
    url: NotRequired[str | None]
