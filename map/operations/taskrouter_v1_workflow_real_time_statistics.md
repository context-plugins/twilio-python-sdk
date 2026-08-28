<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1WorkflowRealTimeStatistics — operations

Accessor: `client.taskrouter_v1_workflow_real_time_statistics` · Source: `twilio_sdk/apis/taskrouter_v1_workflow_real_time_statistics.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_workflow_real_time_statistics.fetch_workflow_real_time_statistics

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/RealTimeStatistics`
- **Server**: `default8`
- **Signature**: `def fetch_workflow_real_time_statistics(workspace_sid: str, workflow_sid: str, *, task_channel: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `workflow_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `workflow_sid` — path `WorkflowSid` · `task_channel` — query `TaskChannel`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics` | `twilio_sdk/models/taskrouter_v1_workspace_workflow_workflow_real_time_statistics.py` |

