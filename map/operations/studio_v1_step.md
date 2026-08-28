<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV1Step — operations

Accessor: `client.studio_v1_step` · Source: `twilio_sdk/apis/studio_v1_step.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.studio_v1_step.fetch_step

- **Route**: `GET /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps/{Sid}`
- **Server**: `default11`
- **Signature**: `def fetch_step(flow_sid: str, engagement_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `engagement_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `engagement_sid` — path `EngagementSid` · `sid` — path `Sid`
- **Returns (parsed)**: `StudioV1FlowEngagementStep`
- **Returns (raw)**: `ApiResult[StudioV1FlowEngagementStep, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowEngagementStep` | `twilio_sdk/models/studio_v1_flow_engagement_step.py` |

### client.studio_v1_step.list_step

- **Route**: `GET /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps`
- **Server**: `default11`
- **Signature**: `def list_step(flow_sid: str, engagement_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `engagement_sid`
- **Params**: `flow_sid` — path `FlowSid` · `engagement_sid` — path `EngagementSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListStepResponse`
- **Returns (raw)**: `ApiResult[ListStepResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListStepResponse` | `twilio_sdk/models/list_step_response.py` |

