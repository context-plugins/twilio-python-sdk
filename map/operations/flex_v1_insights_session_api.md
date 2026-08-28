<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InsightsSessionApi — operations

Accessor: `client.flex_v1_insights_session_api` · Source: `twilio_sdk/apis/flex_v1_insights_session_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_insights_session_api.create_insights_session

- **Route**: `POST /v1/Insights/Session`
- **Server**: `default13`
- **Signature**: `def create_insights_session(*, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `authorization` — header `Authorization`
- **Returns (parsed)**: `FlexV1InsightsSession`
- **Returns (raw)**: `ApiResult[FlexV1InsightsSession, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsSession` | `twilio_sdk/models/flex_v1_insights_session.py` |

