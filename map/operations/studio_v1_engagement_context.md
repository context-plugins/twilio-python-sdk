<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV1EngagementContext — operations

Accessor: `client.studio_v1_engagement_context` · Source: `twilio/apis/studio_v1_engagement_context.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.studio_v1_engagement_context.fetch_engagement_context

- **Route**: `GET /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Context`
- **Server**: `default11`
- **Signature**: `def fetch_engagement_context(flow_sid: str, engagement_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `engagement_sid`
- **Params**: `flow_sid` — path `FlowSid` · `engagement_sid` — path `EngagementSid`
- **Returns (parsed)**: `StudioV1FlowEngagementEngagementContext`
- **Returns (raw)**: `ApiResult[StudioV1FlowEngagementEngagementContext, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowEngagementEngagementContext` | `twilio/models/studio_v1_flow_engagement_engagement_context.py` |

