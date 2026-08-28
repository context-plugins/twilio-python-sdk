from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

CreateLookupPhoneNumberOverridesErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateLookupPhoneNumberOverridesError:
    def map(self, response: HttpResponse) -> CreateLookupPhoneNumberOverridesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


create_lookup_phone_number_overrides_error_mapper: Final[
    ErrorMapper[CreateLookupPhoneNumberOverridesErrorBody]
] = _CreateLookupPhoneNumberOverridesError()
