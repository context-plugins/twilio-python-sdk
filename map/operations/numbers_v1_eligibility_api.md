<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1EligibilityApi — operations

Accessor: `client.numbers_v1_eligibility_api` · Source: `twilio_sdk/apis/numbers_v1_eligibility_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_eligibility_api.create_eligibility

- **Route**: `POST /v1/HostedNumber/Eligibility`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def create_eligibility(*, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NumbersV1Eligibility`
- **Returns (raw)**: `ApiResult[NumbersV1Eligibility, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1Eligibility` | `twilio_sdk/models/numbers_v1_eligibility.py` |

