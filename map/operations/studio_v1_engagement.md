<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV1Engagement — operations

Accessor: `client.studio_v1_engagement` · Source: `twilio_sdk/apis/studio_v1_engagement.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.studio_v1_engagement.create_engagement

- **Route**: `POST /v1/Flows/{FlowSid}/Engagements`
- **Server**: `default11`
- **Signature**: `def create_engagement(flow_sid: str, to: str, from_: str, *, parameters: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `to`, `from_`
- **Params**: `flow_sid` — path `FlowSid` · `to` — form field `To` · `from_` — form field `From` · `parameters` — form field `Parameters`
- **Returns (parsed)**: `StudioV1FlowEngagement`
- **Returns (raw)**: `ApiResult[StudioV1FlowEngagement, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowEngagement` | `twilio_sdk/models/studio_v1_flow_engagement.py` |

### client.studio_v1_engagement.delete_engagement

- **Route**: `DELETE /v1/Flows/{FlowSid}/Engagements/{Sid}`
- **Server**: `default11`
- **Signature**: `def delete_engagement(flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.studio_v1_engagement.fetch_engagement

- **Route**: `GET /v1/Flows/{FlowSid}/Engagements/{Sid}`
- **Server**: `default11`
- **Signature**: `def fetch_engagement(flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid`
- **Returns (parsed)**: `StudioV1FlowEngagement`
- **Returns (raw)**: `ApiResult[StudioV1FlowEngagement, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowEngagement` | `twilio_sdk/models/studio_v1_flow_engagement.py` |

### client.studio_v1_engagement.list_engagement

- **Route**: `GET /v1/Flows/{FlowSid}/Engagements`
- **Server**: `default11`
- **Signature**: `def list_engagement(flow_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`
- **Params**: `flow_sid` — path `FlowSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEngagementResponse`
- **Returns (raw)**: `ApiResult[ListEngagementResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEngagementResponse` | `twilio_sdk/models/list_engagement_response.py` |

