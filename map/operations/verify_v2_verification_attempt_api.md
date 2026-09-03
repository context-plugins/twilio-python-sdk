<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2VerificationAttemptApi — operations

Accessor: `client.verify_v2_verification_attempt_api` · Source: `twilio_sdk/apis/verify_v2_verification_attempt_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_verification_attempt_api.fetch_verification_attempt

- **Route**: `GET /v2/Attempts/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def fetch_verification_attempt(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2VerificationAttempt`
- **Returns (raw)**: `ApiResult[VerifyV2VerificationAttempt, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2VerificationAttempt` | `twilio_sdk/models/verify_v2_verification_attempt.py` |

### client.verify_v2_verification_attempt_api.list_verification_attempt

- **Route**: `GET /v2/Attempts`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def list_verification_attempt(*, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, channel_data_to: str | None = None, country: str | None = None, channel: VerificationAttemptEnumChannelsOrStr | None = None, verify_service_sid: str | None = None, verification_sid: str | None = None, status: VerificationAttemptEnumConversionStatusOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `channel_data_to` — query `ChannelData.To` · `country` — query `Country` · `channel` — query `Channel` · `verify_service_sid` — query `VerifyServiceSid` · `verification_sid` — query `VerificationSid` · `status` — query `Status` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListVerificationAttemptResponse`
- **Returns (raw)**: `ApiResult[ListVerificationAttemptResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerificationAttemptEnumChannelsOrStr` | `twilio_sdk/models/enums/verification_attempt_enum_channels.py` |
| `VerificationAttemptEnumConversionStatusOrStr` | `twilio_sdk/models/enums/verification_attempt_enum_conversion_status.py` |
| `ListVerificationAttemptResponse` | `twilio_sdk/models/list_verification_attempt_response.py` |

