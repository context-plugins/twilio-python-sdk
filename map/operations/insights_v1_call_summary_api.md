<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1CallSummaryApi — operations

Accessor: `client.insights_v1_call_summary_api` · Source: `twilio_sdk/apis/insights_v1_call_summary_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_call_summary_api.fetch_summary

- **Route**: `GET /v1/Voice/{CallSid}/Summary`
- **Server**: `default14`
- **Signature**: `def fetch_summary(call_sid: str, *, processing_state: SummaryEnumProcessingStateOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `call_sid`
- **Params**: `call_sid` — path `CallSid` · `processing_state` — query `ProcessingState`
- **Returns (parsed)**: `InsightsV1CallSummary`
- **Returns (raw)**: `ApiResult[InsightsV1CallSummary, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SummaryEnumProcessingStateOrStr` | `twilio_sdk/models/enums/summary_enum_processing_state.py` |
| `InsightsV1CallSummary` | `twilio_sdk/models/insights_v1_call_summary.py` |

