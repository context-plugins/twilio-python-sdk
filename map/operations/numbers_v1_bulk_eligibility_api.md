<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1BulkEligibilityApi — operations

Accessor: `client.numbers_v1_bulk_eligibility_api` · Source: `twilio_sdk/apis/numbers_v1_bulk_eligibility_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_bulk_eligibility_api.create_bulk_eligibility

- **Route**: `POST /v1/HostedNumber/Eligibility/Bulk`
- **Server**: `default5`
- **Signature**: `def create_bulk_eligibility(*, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NumbersV1BulkEligibility`
- **Returns (raw)**: `ApiResult[NumbersV1BulkEligibility, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1BulkEligibility` | `twilio_sdk/models/numbers_v1_bulk_eligibility.py` |

### client.numbers_v1_bulk_eligibility_api.fetch_bulk_eligibility

- **Route**: `GET /v1/HostedNumber/Eligibility/Bulk/{RequestId}`
- **Server**: `default5`
- **Signature**: `def fetch_bulk_eligibility(request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `request_id`
- **Params**: `request_id` — path `RequestId`
- **Returns (parsed)**: `NumbersV1BulkEligibility`
- **Returns (raw)**: `ApiResult[NumbersV1BulkEligibility, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1BulkEligibility` | `twilio_sdk/models/numbers_v1_bulk_eligibility.py` |

