from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.message_feedback_enum_outcome import MessageFeedbackEnumOutcomeOrStr


class ApiV2010AccountMessageMessageFeedback(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with this MessageFeedback
    resource."""

    message_sid: OptionalNullable[str] = UNSET
    """The SID of the Message resource associated with this MessageFeedback resource."""

    outcome: Optional[MessageFeedbackEnumOutcomeOrStr] = UNSET
    """Reported outcome indicating whether there is confirmation that the Message recipient performed a tracked user
    action. Can be: ``unconfirmed`` or ``confirmed``. For more details see `How to Optimize Message Deliverability with
    Message Feedback <https://www.twilio.com/docs/messaging/guides/send-message-feedback-to-twilio>`__."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT when this MessageFeedback resource was created, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT when this MessageFeedback resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountMessageMessageFeedbackDict(TypedDict):
    account_sid: NotRequired[str | None]
    message_sid: NotRequired[str | None]
    outcome: NotRequired[MessageFeedbackEnumOutcomeOrStr]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    uri: NotRequired[str | None]
