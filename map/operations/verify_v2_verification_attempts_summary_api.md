<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2VerificationAttemptsSummaryApi — operations

Accessor: `client.verify_v2_verification_attempts_summary_api` · Source: `twilio_sdk/apis/verify_v2_verification_attempts_summary_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_verification_attempts_summary_api.fetch_verification_attempts_summary

- **Route**: `GET /v2/Attempts/Summary`
- **Server**: `default3`
- **Signature**: `def fetch_verification_attempts_summary(*, verify_service_sid: str | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, country: str | None = None, channel: VerificationAttemptsSummaryEnumChannelsOrStr | None = None, destination_prefix: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `verify_service_sid` — query `VerifyServiceSid` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `country` — query `Country` · `channel` — query `Channel` · `destination_prefix` — query `DestinationPrefix`
- **Returns (parsed)**: `VerifyV2VerificationAttemptsSummary`
- **Returns (raw)**: `ApiResult[VerifyV2VerificationAttemptsSummary, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerificationAttemptsSummaryEnumChannelsOrStr` | `twilio_sdk/models/enums/verification_attempts_summary_enum_channels.py` |
| `VerifyV2VerificationAttemptsSummary` | `twilio_sdk/models/verify_v2_verification_attempts_summary.py` |

