from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.interaction_transfer_enum_transfer_status import InteractionTransferEnumTransferStatusOrStr
from .enums.interaction_transfer_enum_transfer_type import InteractionTransferEnumTransferTypeOrStr


class FlexV1InteractionInteractionChannelInteractionTransfer(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string created by Twilio to identify an Interaction Transfer resource."""

    instance_sid: OptionalNullable[str] = UNSET
    """The SID of the Instance associated with the Transfer."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the Account that created the Transfer."""

    interaction_sid: OptionalNullable[str] = UNSET
    """The Interaction Sid for this channel."""

    channel_sid: OptionalNullable[str] = UNSET
    """The Channel Sid for this Transfer."""

    execution_sid: OptionalNullable[str] = UNSET
    """The Execution SID associated with the Transfer."""

    type_: Optional[InteractionTransferEnumTransferTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of the Transfer. Can be: ``cold``, ``warm``."""

    status: Optional[InteractionTransferEnumTransferStatusOrStr] = UNSET
    """The status of the Transfer. Can be: ``active``, ``completed``, ``failed``."""

    from_: OptionalNullable[str] = Field(default=UNSET, alias="from")
    """The SID of the Participant initiating the Transfer."""

    to: OptionalNullable[str] = UNSET
    """The SID of the Participant receiving the Transfer."""

    note_sid: OptionalNullable[str] = UNSET
    """The SID of the Note associated with the Transfer."""

    summary_sid: OptionalNullable[str] = UNSET
    """The SID of the Summary associated with the Transfer."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time when the Transfer was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time when the Transfer was last updated."""

    url: OptionalNullable[str] = UNSET


class FlexV1InteractionInteractionChannelInteractionTransferDict(TypedDict):
    sid: NotRequired[str | None]
    instance_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    interaction_sid: NotRequired[str | None]
    channel_sid: NotRequired[str | None]
    execution_sid: NotRequired[str | None]
    type_: NotRequired[InteractionTransferEnumTransferTypeOrStr]
    status: NotRequired[InteractionTransferEnumTransferStatusOrStr]
    from_: NotRequired[str | None]
    to: NotRequired[str | None]
    note_sid: NotRequired[str | None]
    summary_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
