<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV1Execution — operations

Accessor: `client.studio_v1_execution` · Source: `twilio/apis/studio_v1_execution.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.studio_v1_execution.create_execution

- **Route**: `POST /v1/Flows/{FlowSid}/Executions`
- **Server**: `default11`
- **Signature**: `def create_execution(flow_sid: str, to: str, from_: str, *, parameters: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `to`, `from_`
- **Params**: `flow_sid` — path `FlowSid` · `to` — form field `To` · `from_` — form field `From` · `parameters` — form field `Parameters`
- **Returns (parsed)**: `StudioV1FlowExecution`
- **Returns (raw)**: `ApiResult[StudioV1FlowExecution, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowExecution` | `twilio/models/studio_v1_flow_execution.py` |

### client.studio_v1_execution.delete_execution

- **Route**: `DELETE /v1/Flows/{FlowSid}/Executions/{Sid}`
- **Server**: `default11`
- **Signature**: `def delete_execution(flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.studio_v1_execution.fetch_execution

- **Route**: `GET /v1/Flows/{FlowSid}/Executions/{Sid}`
- **Server**: `default11`
- **Signature**: `def fetch_execution(flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid`
- **Returns (parsed)**: `StudioV1FlowExecution`
- **Returns (raw)**: `ApiResult[StudioV1FlowExecution, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowExecution` | `twilio/models/studio_v1_flow_execution.py` |

### client.studio_v1_execution.list_execution

- **Route**: `GET /v1/Flows/{FlowSid}/Executions`
- **Server**: `default11`
- **Signature**: `def list_execution(flow_sid: str, *, date_created_from: RFC3339DateTime | None = None, date_created_to: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`
- **Params**: `flow_sid` — path `FlowSid` · `date_created_from` — query `DateCreatedFrom` · `date_created_to` — query `DateCreatedTo` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListExecutionResponse`
- **Returns (raw)**: `ApiResult[ListExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListExecutionResponse` | `twilio/models/list_execution_response.py` |

### client.studio_v1_execution.update_execution

- **Route**: `POST /v1/Flows/{FlowSid}/Executions/{Sid}`
- **Server**: `default11`
- **Signature**: `def update_execution(flow_sid: str, sid: str, status: ExecutionEnumStatusOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `sid`, `status`
- **Params**: `flow_sid` — path `FlowSid` · `sid` — path `Sid` · `status` — form field `Status`
- **Returns (parsed)**: `StudioV1FlowExecution`
- **Returns (raw)**: `ApiResult[StudioV1FlowExecution, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ExecutionEnumStatusOrStr` | `twilio/models/enums/execution_enum_status.py` |
| `StudioV1FlowExecution` | `twilio/models/studio_v1_flow_execution.py` |

