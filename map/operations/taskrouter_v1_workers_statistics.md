<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1WorkersStatistics — operations

Accessor: `client.taskrouter_v1_workers_statistics` · Source: `twilio/apis/taskrouter_v1_workers_statistics.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_workers_statistics.fetch_worker_statistics

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workers/Statistics`
- **Server**: `default8`
- **Signature**: `def fetch_worker_statistics(workspace_sid: str, *, minutes: int | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, task_queue_sid: str | None = None, task_queue_name: str | None = None, friendly_name: str | None = None, task_channel: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `minutes` — query `Minutes` · `start_date` — query `StartDate` · `end_date` — query `EndDate` · `task_queue_sid` — query `TaskQueueSid` · `task_queue_name` — query `TaskQueueName` · `friendly_name` — query `FriendlyName` · `task_channel` — query `TaskChannel`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorkerWorkerStatistics`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorkerWorkerStatistics, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorkerWorkerStatistics` | `twilio/models/taskrouter_v1_workspace_worker_worker_statistics.py` |

