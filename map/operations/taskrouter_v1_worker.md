<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1Worker — operations

Accessor: `client.taskrouter_v1_worker` · Source: `twilio_sdk/apis/taskrouter_v1_worker.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.taskrouter_v1_worker.create_worker

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Workers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def create_worker(workspace_sid: str, friendly_name: str, *, activity_sid: str | None = None, attributes: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `friendly_name`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `friendly_name` — form field `FriendlyName` · `activity_sid` — form field `ActivitySid` · `attributes` — form field `Attributes`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorker`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorker, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorker` | `twilio_sdk/models/taskrouter_v1_workspace_worker.py` |

### client.taskrouter_v1_worker.delete_worker

- **Route**: `DELETE /v1/Workspaces/{WorkspaceSid}/Workers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def delete_worker(workspace_sid: str, sid: str, *, if_match: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid` · `if_match` — header `If-Match`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.taskrouter_v1_worker.fetch_worker

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def fetch_worker(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorker`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorker, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorker` | `twilio_sdk/models/taskrouter_v1_workspace_worker.py` |

### client.taskrouter_v1_worker.list_worker

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def list_worker(workspace_sid: str, *, activity_name: str | None = None, activity_sid: str | None = None, available: str | None = None, friendly_name: str | None = None, target_workers_expression: str | None = None, task_queue_name: str | None = None, task_queue_sid: str | None = None, ordering: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `activity_name` — query `ActivityName` · `activity_sid` — query `ActivitySid` · `available` — query `Available` · `friendly_name` — query `FriendlyName` · `target_workers_expression` — query `TargetWorkersExpression` · `task_queue_name` — query `TaskQueueName` · `task_queue_sid` — query `TaskQueueSid` · `ordering` — query `Ordering` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListWorkerResponse`
- **Returns (raw)**: `ApiResult[ListWorkerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWorkerResponse` | `twilio_sdk/models/list_worker_response.py` |

### client.taskrouter_v1_worker.update_worker

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Workers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def update_worker(workspace_sid: str, sid: str, *, if_match: str | None = None, activity_sid: str | None = None, attributes: str | None = None, friendly_name: str | None = None, reject_pending_reservations: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid` · `if_match` — header `If-Match` · `activity_sid` — form field `ActivitySid` · `attributes` — form field `Attributes` · `friendly_name` — form field `FriendlyName` · `reject_pending_reservations` — form field `RejectPendingReservations`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorker`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorker, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorker` | `twilio_sdk/models/taskrouter_v1_workspace_worker.py` |

