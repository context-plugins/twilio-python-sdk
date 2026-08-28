from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

FetchConversationActionErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _FetchConversationActionError:
    def map(self, response: HttpResponse) -> FetchConversationActionErrorBody:
        match response.status_code:
            case 400 | 404 | 429 | 500 | 503:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


fetch_conversation_action_error_mapper: Final[
    ErrorMapper[FetchConversationActionErrorBody]
] = _FetchConversationActionError()
