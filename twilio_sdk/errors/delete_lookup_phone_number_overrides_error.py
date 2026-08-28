from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.accounts_calls_recordings_sid_json201041408_error1 import AccountsCallsRecordingsSidJson201041408Error1

DeleteLookupPhoneNumberOverridesErrorBody: TypeAlias = AccountsCallsRecordingsSidJson201041408Error1 | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLookupPhoneNumberOverridesError:
    def map(self, response: HttpResponse) -> DeleteLookupPhoneNumberOverridesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[AccountsCallsRecordingsSidJson201041408Error1](response)
            case _:
                return RawError(response)


delete_lookup_phone_number_overrides_error_mapper: Final[
    ErrorMapper[DeleteLookupPhoneNumberOverridesErrorBody]
] = _DeleteLookupPhoneNumberOverridesError()
