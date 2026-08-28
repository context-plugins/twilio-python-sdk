<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV2Execution — operations

Accessor: `client.studio_v2_execution` · Source: `twilio_sdk/apis/studio_v2_execution.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.studio_v2_execution.create_execution2

- **Route**: `POST /v2/Flows/{FlowSid}/Executions`
- **Server**: `default11`
- **Signature**: `def create_execution2(flow_sid: str, to: str, from_: str, *, parameters: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `to`, `from_`
- **Params**: `flow_sid` — path `FlowSid` · `to` — form field `To` · `from_` — form field `From` · `parameters` — form field `Parameters`
- **Returns (parsed)**: `StudioV2FlowExecution`
- **Returns (raw)**: `ApiResult[StudioV2FlowExecution, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV2FlowExecution` | `twilio_sdk/models/studio_v2_flow_execution.py` |

### client.studio_v2_execution.delete_execution2

- **Route**: `DELETE /v2/Flows/{FlowSid}/Executions/{Sid}`
- **Server**: `default11`
- **Signature**: `def delete_execution2(flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.studio_v2_execution.fetch_execution2

- **Route**: `GET /v2/Flows/{FlowSid}/Executions/{Sid}`
- **Server**: `default11`
- **Signature**: `def fetch_execution2(flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid`
- **Returns (parsed)**: `StudioV2FlowExecution`
- **Returns (raw)**: `ApiResult[StudioV2FlowExecution, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV2FlowExecution` | `twilio_sdk/models/studio_v2_flow_execution.py` |

### client.studio_v2_execution.list_execution2

- **Route**: `GET /v2/Flows/{FlowSid}/Executions`
- **Server**: `default11`
- **Signature**: `def list_execution2(flow_sid: str, *, status: EngagementEnumStatusOrStr | None = None, date_created_from: RFC3339DateTime | None = None, date_created_to: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`
- **Params**: `flow_sid` — path `FlowSid` · `status` — query · `date_created_from` — query `DateCreatedFrom` · `date_created_to` — query `DateCreatedTo` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListExecutionResponse1`
- **Returns (raw)**: `ApiResult[ListExecutionResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EngagementEnumStatusOrStr` | `twilio_sdk/models/enums/engagement_enum_status.py` |
| `ListExecutionResponse1` | `twilio_sdk/models/list_execution_response1.py` |

### client.studio_v2_execution.update_execution2

- **Route**: `POST /v2/Flows/{FlowSid}/Executions/{Sid}`
- **Server**: `default11`
- **Signature**: `def update_execution2(flow_sid: str, sid: str, status: EngagementEnumStatusOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`, `status`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid` · `status` — form field `Status`
- **Returns (parsed)**: `StudioV2FlowExecution`
- **Returns (raw)**: `ApiResult[StudioV2FlowExecution, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EngagementEnumStatusOrStr` | `twilio_sdk/models/enums/engagement_enum_status.py` |
| `StudioV2FlowExecution` | `twilio_sdk/models/studio_v2_flow_execution.py` |

