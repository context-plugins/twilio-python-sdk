from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

ListCommunicationByConversationErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ListCommunicationByConversationError:
    def map(self, response: HttpResponse) -> ListCommunicationByConversationErrorBody:
        match response.status_code:
            case 400 | 404 | 429 | 500 | 503:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


list_communication_by_conversation_error_mapper: Final[
    ErrorMapper[ListCommunicationByConversationErrorBody]
] = _ListCommunicationByConversationError()
