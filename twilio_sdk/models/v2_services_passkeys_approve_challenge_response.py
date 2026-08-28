from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.challenge_enum_challenge_reasons import ChallengeEnumChallengeReasonsOrStr
from .enums.challenge_enum_challenge_statuses import ChallengeEnumChallengeStatusesOrStr
from .enums.challenge_enum_factor_types import ChallengeEnumFactorTypesOrStr


class V2ServicesPasskeysApproveChallengeResponse(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this Challenge."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    service_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Service."""

    entity_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Entity."""

    identity: OptionalNullable[str] = UNSET
    """Customer unique identity for the Entity owner of the Challenge."""

    factor_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Factor."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this Challenge was created, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this Challenge was updated, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""

    date_responded: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this Challenge was responded, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""

    expiration_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The date-time when this Challenge expires, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""

    status: Optional[ChallengeEnumChallengeStatusesOrStr] = UNSET
    """The Status of this Challenge. One of ``pending``, ``expired``, ``approved`` or ``denied``."""

    responded_reason: Optional[ChallengeEnumChallengeReasonsOrStr] = UNSET
    """Reason for the Challenge to be in certain ``status``. One of ``none``, ``not_needed`` or ``not_requested``."""

    details: OptionalNullable[Any] = UNSET
    """Details provided to give context about the Challenge."""

    hidden_details: OptionalNullable[Any] = UNSET
    """Details provided to give context about the Challenge."""

    metadata: OptionalNullable[Any] = UNSET
    """Custom metadata associated with the challenge."""

    factor_type: Optional[ChallengeEnumFactorTypesOrStr] = UNSET
    """The Factor Type of this Challenge. Currently ``push`` and ``totp`` are supported."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""

    links: OptionalNullable[Any] = UNSET
    """Contains a dictionary of URL links to nested resources of this Challenge."""

    options: Optional[Any] = UNSET
    """An object that contains challenge options. Currently only used for ``passkeys``."""


class V2ServicesPasskeysApproveChallengeResponseDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    entity_sid: NotRequired[str | None]
    identity: NotRequired[str | None]
    factor_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    date_responded: NotRequired[RFC3339DateTime | None]
    expiration_date: NotRequired[RFC3339DateTime | None]
    status: NotRequired[ChallengeEnumChallengeStatusesOrStr]
    responded_reason: NotRequired[ChallengeEnumChallengeReasonsOrStr]
    details: NotRequired[Any | None]
    hidden_details: NotRequired[Any | None]
    metadata: NotRequired[Any | None]
    factor_type: NotRequired[ChallengeEnumFactorTypesOrStr]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
    options: NotRequired[Any]
