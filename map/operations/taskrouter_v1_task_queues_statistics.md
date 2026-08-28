<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1TaskQueuesStatistics — operations

Accessor: `client.taskrouter_v1_task_queues_statistics` · Source: `twilio_sdk/apis/taskrouter_v1_task_queues_statistics.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_task_queues_statistics.list_task_queues_statistics

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/TaskQueues/Statistics`
- **Server**: `default8`
- **Signature**: `def list_task_queues_statistics(workspace_sid: str, *, end_date: RFC3339DateTime | None = None, friendly_name: str | None = None, minutes: int | None = None, start_date: RFC3339DateTime | None = None, task_channel: str | None = None, split_by_wait_time: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `end_date` — query `EndDate` · `friendly_name` — query `FriendlyName` · `minutes` — query `Minutes` · `start_date` — query `StartDate` · `task_channel` — query `TaskChannel` · `split_by_wait_time` — query `SplitByWaitTime` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTaskQueuesStatisticsResponse`
- **Returns (raw)**: `ApiResult[ListTaskQueuesStatisticsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTaskQueuesStatisticsResponse` | `twilio_sdk/models/list_task_queues_statistics_response.py` |

