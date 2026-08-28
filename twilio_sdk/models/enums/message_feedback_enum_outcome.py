from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageFeedbackEnumOutcome(str, Enum):
    """Reported outcome indicating whether there is confirmation that the Message recipient performed a tracked user
    action. Can be: ``unconfirmed`` or ``confirmed``. For more details see `How to Optimize Message Deliverability with
    Message Feedback <https://www.twilio.com/docs/messaging/guides/send-message-feedback-to-twilio>`__."""

    CONFIRMED = "confirmed"
    UNCONFIRMED = "unconfirmed"

    __str__ = str.__str__


MessageFeedbackEnumOutcomeOrStr: TypeAlias = Annotated[
    MessageFeedbackEnumOutcome | str, open_enum_validator(MessageFeedbackEnumOutcome)
]
