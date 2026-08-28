<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1CallApi — operations

Accessor: `client.insights_v1_call_api` · Source: `twilio_sdk/apis/insights_v1_call_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_call_api.fetch_call2

- **Route**: `GET /v1/Voice/{Sid}`
- **Server**: `default14`
- **Signature**: `def fetch_call2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `InsightsV1Call`
- **Returns (raw)**: `ApiResult[InsightsV1Call, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1Call` | `twilio_sdk/models/insights_v1_call.py` |

