from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

CreateV3TypingIndicatorErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateV3TypingIndicatorError:
    def map(self, response: HttpResponse) -> CreateV3TypingIndicatorErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


create_v3_typing_indicator_error_mapper: Final[
    ErrorMapper[CreateV3TypingIndicatorErrorBody]
] = _CreateV3TypingIndicatorError()
