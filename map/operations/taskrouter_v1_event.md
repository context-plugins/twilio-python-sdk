<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1Event — operations

Accessor: `client.taskrouter_v1_event` · Source: `twilio_sdk/apis/taskrouter_v1_event.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_event.fetch_event

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Events/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def fetch_event(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceEvent`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceEvent, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceEvent` | `twilio_sdk/models/taskrouter_v1_workspace_event.py` |

### client.taskrouter_v1_event.list_event

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Events`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def list_event(workspace_sid: str, *, end_date: RFC3339DateTime | None = None, event_type: str | None = None, minutes: int | None = None, reservation_sid: str | None = None, start_date: RFC3339DateTime | None = None, task_queue_sid: str | None = None, task_sid: str | None = None, worker_sid: str | None = None, workflow_sid: str | None = None, task_channel: str | None = None, sid: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `end_date` — query `EndDate` · `event_type` — query `EventType` · `minutes` — query `Minutes` · `reservation_sid` — query `ReservationSid` · `start_date` — query `StartDate` · `task_queue_sid` — query `TaskQueueSid` · `task_sid` — query `TaskSid` · `worker_sid` — query `WorkerSid` · `workflow_sid` — query `WorkflowSid` · `task_channel` — query `TaskChannel` · `sid` — query `Sid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEventResponse`
- **Returns (raw)**: `ApiResult[ListEventResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEventResponse` | `twilio_sdk/models/list_event_response.py` |

