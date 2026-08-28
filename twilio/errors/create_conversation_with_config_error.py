from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

CreateConversationWithConfigErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateConversationWithConfigError:
    def map(self, response: HttpResponse) -> CreateConversationWithConfigErrorBody:
        match response.status_code:
            case 400 | 404 | 409 | 429 | 500 | 503:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


create_conversation_with_config_error_mapper: Final[
    ErrorMapper[CreateConversationWithConfigErrorBody]
] = _CreateConversationWithConfigError()
