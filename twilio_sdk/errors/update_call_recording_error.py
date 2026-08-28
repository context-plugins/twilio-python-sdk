from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

UpdateCallRecordingErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCallRecordingError:
    def map(self, response: HttpResponse) -> UpdateCallRecordingErrorBody:
        match response.status_code:
            case 408:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


update_call_recording_error_mapper: Final[ErrorMapper[UpdateCallRecordingErrorBody]] = _UpdateCallRecordingError()
