<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1TaskQueueBulkRealTimeStatistics — operations

Accessor: `client.taskrouter_v1_task_queue_bulk_real_time_statistics` · Source: `twilio_sdk/apis/taskrouter_v1_task_queue_bulk_real_time_statistics.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_task_queue_bulk_real_time_statistics.create_task_queue_bulk_real_time_statistics

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/TaskQueues/RealTimeStatistics`
- **Server**: `default8`
- **Signature**: `def create_task_queue_bulk_real_time_statistics(workspace_sid: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `body` — JSON body
- **Returns (parsed)**: `TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics` | `twilio_sdk/models/taskrouter_v1_workspace_task_queue_task_queue_bulk_real_time_statistics.py` |

