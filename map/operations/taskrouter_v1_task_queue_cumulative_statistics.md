<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1TaskQueueCumulativeStatistics — operations

Accessor: `client.taskrouter_v1_task_queue_cumulative_statistics` · Source: `twilio/apis/taskrouter_v1_task_queue_cumulative_statistics.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_task_queue_cumulative_statistics.fetch_task_queue_cumulative_statistics

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/CumulativeStatistics`
- **Server**: `default8`
- **Signature**: `def fetch_task_queue_cumulative_statistics(workspace_sid: str, task_queue_sid: str, *, end_date: RFC3339DateTime | None = None, minutes: int | None = None, start_date: RFC3339DateTime | None = None, task_channel: str | None = None, split_by_wait_time: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `task_queue_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `task_queue_sid` — path `TaskQueueSid` · `end_date` — query `EndDate` · `minutes` — query `Minutes` · `start_date` — query `StartDate` · `task_channel` — query `TaskChannel` · `split_by_wait_time` — query `SplitByWaitTime`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics` | `twilio/models/taskrouter_v1_workspace_task_queue_task_queue_cumulative_statistics.py` |

