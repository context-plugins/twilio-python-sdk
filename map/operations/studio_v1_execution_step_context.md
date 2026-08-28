<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV1ExecutionStepContext — operations

Accessor: `client.studio_v1_execution_step_context` · Source: `twilio/apis/studio_v1_execution_step_context.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.studio_v1_execution_step_context.fetch_execution_step_context

- **Route**: `GET /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{StepSid}/Context`
- **Server**: `default11`
- **Signature**: `def fetch_execution_step_context(flow_sid: str, execution_sid: str, step_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flow_sid`, `execution_sid`, `step_sid`
- **Params**: `flow_sid` — path `FlowSid` · `execution_sid` — path `ExecutionSid` · `step_sid` — path `StepSid`
- **Returns (parsed)**: `StudioV1FlowExecutionExecutionStepExecutionStepContext`
- **Returns (raw)**: `ApiResult[StudioV1FlowExecutionExecutionStepExecutionStepContext, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1FlowExecutionExecutionStepExecutionStepContext` | `twilio/models/studio_v1_flow_execution_execution_step_execution_step_context.py` |

