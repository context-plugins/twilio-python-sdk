<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV1ExecutionStep — operations

Accessor: `client.studio_v1_execution_step` · Source: `twilio_sdk/apis/studio_v1_execution_step.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.studio_v1_execution_step.fetch_execution_step

- **Route**: `GET /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default11`
- **Signature**: `def fetch_execution_step(flow_sid: str, execution_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `execution_sid`, `sid`
- **Params**: `flow_sid` — path `FlowSid` · `execution_sid` — path `ExecutionSid` · `sid` — path `Sid`
- **Returns (parsed)**: `StudioV1FlowExecutionExecutionStep`
- **Returns (raw)**: `ApiResult[StudioV1FlowExecutionExecutionStep, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowExecutionExecutionStep` | `twilio_sdk/models/studio_v1_flow_execution_execution_step.py` |

### client.studio_v1_execution_step.list_execution_step

- **Route**: `GET /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps`
- **Auth**: `account_sid_auth_token`
- **Server**: `default11`
- **Signature**: `def list_execution_step(flow_sid: str, execution_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `execution_sid`
- **Params**: `flow_sid` — path `FlowSid` · `execution_sid` — path `ExecutionSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListExecutionStepResponse`
- **Returns (raw)**: `ApiResult[ListExecutionStepResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListExecutionStepResponse` | `twilio_sdk/models/list_execution_step_response.py` |

