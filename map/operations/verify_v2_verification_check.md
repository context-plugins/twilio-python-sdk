<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2VerificationCheck — operations

Accessor: `client.verify_v2_verification_check` · Source: `twilio_sdk/apis/verify_v2_verification_check.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_verification_check.create_verification_check

- **Route**: `POST /v2/Services/{ServiceSid}/VerificationCheck`
- **Server**: `default3`
- **Signature**: `def create_verification_check(service_sid: str, *, code: str | None = None, to: str | None = None, verification_sid: str | None = None, amount: str | None = None, payee: str | None = None, sna_client_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `code` — form field `Code` · `to` — form field `To` · `verification_sid` — form field `VerificationSid` · `amount` — form field `Amount` · `payee` — form field `Payee` · `sna_client_token` — form field `SnaClientToken`
- **Returns (parsed)**: `VerifyV2ServiceVerificationCheck`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceVerificationCheck, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceVerificationCheck` | `twilio_sdk/models/verify_v2_service_verification_check.py` |

