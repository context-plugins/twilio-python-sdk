from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

FetchLookupAccountRateLimitsErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _FetchLookupAccountRateLimitsError:
    def map(self, response: HttpResponse) -> FetchLookupAccountRateLimitsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


fetch_lookup_account_rate_limits_error_mapper: Final[
    ErrorMapper[FetchLookupAccountRateLimitsErrorBody]
] = _FetchLookupAccountRateLimitsError()
