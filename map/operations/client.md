<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `twilio_sdk/client.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.create_bulk_lookup

- **Route**: `POST /v2/batch/query`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def create_bulk_lookup(*, body: LookupRequest | LookupRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LookupResponse1`
- **Returns (raw)**: `ApiResult[LookupResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LookupRequest` | `twilio_sdk/models/lookup_request.py` |
| `LookupRequestDict` | `twilio_sdk/models/lookup_request.py` |
| `LookupResponse1` | `twilio_sdk/models/lookup_response1.py` |

### client.create_lookup_phone_number_overrides

- **Route**: `POST /v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def create_lookup_phone_number_overrides(field: str, phone_number: str, *, body: OverridesRequest | OverridesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`, `phone_number`
- **Params**: `field` — path `Field` · `phone_number` — path `PhoneNumber` · `body` — JSON body
- **Returns (parsed)**: `OverridesResponse`
- **Returns (raw)**: `ApiResult[OverridesResponse, CreateLookupPhoneNumberOverridesErrorBody]`
- **Error**: `CreateLookupPhoneNumberOverridesErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OverridesRequest` | `twilio_sdk/models/overrides_request.py` |
| `OverridesRequestDict` | `twilio_sdk/models/overrides_request.py` |
| `OverridesResponse` | `twilio_sdk/models/overrides_response.py` |
| `CreateLookupPhoneNumberOverridesErrorBody` | `twilio_sdk/errors/create_lookup_phone_number_overrides_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.delete_lookup_phone_number_overrides

- **Route**: `DELETE /v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def delete_lookup_phone_number_overrides(field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`, `phone_number`
- **Params**: `field` — path `Field` · `phone_number` — path `PhoneNumber`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLookupPhoneNumberOverridesErrorBody]`
- **Error**: `DeleteLookupPhoneNumberOverridesErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLookupPhoneNumberOverridesErrorBody` | `twilio_sdk/errors/delete_lookup_phone_number_overrides_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.delete_lookup_rate_limit

- **Route**: `DELETE /v2/RateLimits/Fields/{Field}/Bucket/{Bucket}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def delete_lookup_rate_limit(field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`, `bucket`
- **Params**: `field` — path `Field` · `bucket` — path `Bucket`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLookupRateLimitErrorBody]`
- **Error**: `DeleteLookupRateLimitErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLookupRateLimitErrorBody` | `twilio_sdk/errors/delete_lookup_rate_limit_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.fetch_lookup_account_rate_limits

- **Route**: `GET /v2/RateLimits`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def fetch_lookup_account_rate_limits(*, fields: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `fields` — query `Fields`
- **Returns (parsed)**: `RateLimitListResponse`
- **Returns (raw)**: `ApiResult[RateLimitListResponse, FetchLookupAccountRateLimitsErrorBody]`
- **Error**: `FetchLookupAccountRateLimitsErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RateLimitListResponse` | `twilio_sdk/models/rate_limit_list_response.py` |
| `FetchLookupAccountRateLimitsErrorBody` | `twilio_sdk/errors/fetch_lookup_account_rate_limits_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.fetch_lookup_phone_number_overrides

- **Route**: `GET /v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def fetch_lookup_phone_number_overrides(field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`, `phone_number`
- **Params**: `field` — path `Field` · `phone_number` — path `PhoneNumber`
- **Returns (parsed)**: `OverridesResponse`
- **Returns (raw)**: `ApiResult[OverridesResponse, FetchLookupPhoneNumberOverridesErrorBody]`
- **Error**: `FetchLookupPhoneNumberOverridesErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OverridesResponse` | `twilio_sdk/models/overrides_response.py` |
| `FetchLookupPhoneNumberOverridesErrorBody` | `twilio_sdk/errors/fetch_lookup_phone_number_overrides_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.fetch_lookup_rate_limit

- **Route**: `GET /v2/RateLimits/Fields/{Field}/Bucket/{Bucket}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def fetch_lookup_rate_limit(field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`, `bucket`
- **Params**: `field` — path `Field` · `bucket` — path `Bucket`
- **Returns (parsed)**: `RateLimitResponse`
- **Returns (raw)**: `ApiResult[RateLimitResponse, FetchLookupRateLimitErrorBody]`
- **Error**: `FetchLookupRateLimitErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RateLimitResponse` | `twilio_sdk/models/rate_limit_response.py` |
| `FetchLookupRateLimitErrorBody` | `twilio_sdk/errors/fetch_lookup_rate_limit_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.update_challenge_passkeys

- **Route**: `POST /v2/Services/{ServiceSid}/Passkeys/ApproveChallenge`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def update_challenge_passkeys(service_sid: str, body: ApprovePasskeysChallengeRequest | ApprovePasskeysChallengeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `body`
- **Params**: `service_sid` — path `ServiceSid` · `body` — JSON body
- **Returns (parsed)**: `V2ServicesPasskeysApproveChallengeResponse`
- **Returns (raw)**: `ApiResult[V2ServicesPasskeysApproveChallengeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApprovePasskeysChallengeRequest` | `twilio_sdk/models/approve_passkeys_challenge_request.py` |
| `ApprovePasskeysChallengeRequestDict` | `twilio_sdk/models/approve_passkeys_challenge_request.py` |
| `V2ServicesPasskeysApproveChallengeResponse` | `twilio_sdk/models/v2_services_passkeys_approve_challenge_response.py` |

### client.update_lookup_phone_number_overrides

- **Route**: `PUT /v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def update_lookup_phone_number_overrides(field: str, phone_number: str, *, body: OverridesRequest | OverridesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`, `phone_number`
- **Params**: `field` — path `Field` · `phone_number` — path `PhoneNumber` · `body` — JSON body
- **Returns (parsed)**: `OverridesResponse`
- **Returns (raw)**: `ApiResult[OverridesResponse, UpdateLookupPhoneNumberOverridesErrorBody]`
- **Error**: `UpdateLookupPhoneNumberOverridesErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OverridesRequest` | `twilio_sdk/models/overrides_request.py` |
| `OverridesRequestDict` | `twilio_sdk/models/overrides_request.py` |
| `OverridesResponse` | `twilio_sdk/models/overrides_response.py` |
| `UpdateLookupPhoneNumberOverridesErrorBody` | `twilio_sdk/errors/update_lookup_phone_number_overrides_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.update_lookup_rate_limit

- **Route**: `PUT /v2/RateLimits/Fields/{Field}/Bucket/{Bucket}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def update_lookup_rate_limit(field: str, bucket: str, *, body: RateLimitRequest | RateLimitRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`, `bucket`
- **Params**: `field` — path `Field` · `bucket` — path `Bucket` · `body` — JSON body
- **Returns (parsed)**: `RateLimitResponse`
- **Returns (raw)**: `ApiResult[RateLimitResponse, UpdateLookupRateLimitErrorBody]`
- **Error**: `UpdateLookupRateLimitErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RateLimitRequest` | `twilio_sdk/models/rate_limit_request.py` |
| `RateLimitRequestDict` | `twilio_sdk/models/rate_limit_request.py` |
| `RateLimitResponse` | `twilio_sdk/models/rate_limit_response.py` |
| `UpdateLookupRateLimitErrorBody` | `twilio_sdk/errors/update_lookup_rate_limit_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.update_passkeys_factor

- **Route**: `POST /v2/Services/{ServiceSid}/Passkeys/VerifyFactor`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def update_passkeys_factor(service_sid: str, body: VerifyPasskeysFactorRequest | VerifyPasskeysFactorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `body`
- **Params**: `service_sid` — path `ServiceSid` · `body` — JSON body
- **Returns (parsed)**: `V2ServicesPasskeysVerifyFactorResponse`
- **Returns (raw)**: `ApiResult[V2ServicesPasskeysVerifyFactorResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyPasskeysFactorRequest` | `twilio_sdk/models/verify_passkeys_factor_request.py` |
| `VerifyPasskeysFactorRequestDict` | `twilio_sdk/models/verify_passkeys_factor_request.py` |
| `V2ServicesPasskeysVerifyFactorResponse` | `twilio_sdk/models/v2_services_passkeys_verify_factor_response.py` |

