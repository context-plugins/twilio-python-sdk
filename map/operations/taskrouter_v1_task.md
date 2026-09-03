<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1Task — operations

Accessor: `client.taskrouter_v1_task` · Source: `twilio_sdk/apis/taskrouter_v1_task.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.taskrouter_v1_task.create_task

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Tasks`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def create_task(workspace_sid: str, *, timeout: int | None = None, priority: int | None = None, task_channel: str | None = None, workflow_sid: str | None = None, attributes: str | None = None, virtual_start_time: RFC3339DateTime | None = None, routing_target: str | None = None, ignore_capacity: str | None = None, task_queue_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `timeout` — form field `Timeout` · `priority` — form field `Priority` · `task_channel` — form field `TaskChannel` · `workflow_sid` — form field `WorkflowSid` · `attributes` — form field `Attributes` · `virtual_start_time` — form field `VirtualStartTime` · `routing_target` — form field `RoutingTarget` · `ignore_capacity` — form field `IgnoreCapacity` · `task_queue_sid` — form field `TaskQueueSid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTask`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTask, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTask` | `twilio_sdk/models/taskrouter_v1_workspace_task.py` |

### client.taskrouter_v1_task.delete_task

- **Route**: `DELETE /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def delete_task(workspace_sid: str, sid: str, *, if_match: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid` · `if_match` — header `If-Match`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.taskrouter_v1_task.fetch_task

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def fetch_task(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTask`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTask, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTask` | `twilio_sdk/models/taskrouter_v1_workspace_task.py` |

### client.taskrouter_v1_task.list_task

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Tasks`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def list_task(workspace_sid: str, *, priority: int | None = None, assignment_status: list[str] | None = None, workflow_sid: str | None = None, workflow_name: str | None = None, task_queue_sid: str | None = None, task_queue_name: str | None = None, evaluate_task_attributes: str | None = None, routing_target: str | None = None, ordering: str | None = None, has_addons: bool | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `priority` — query `Priority` · `assignment_status` — query `AssignmentStatus` · `workflow_sid` — query `WorkflowSid` · `workflow_name` — query `WorkflowName` · `task_queue_sid` — query `TaskQueueSid` · `task_queue_name` — query `TaskQueueName` · `evaluate_task_attributes` — query `EvaluateTaskAttributes` · `routing_target` — query `RoutingTarget` · `ordering` — query `Ordering` · `has_addons` — query `HasAddons` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTaskResponse`
- **Returns (raw)**: `ApiResult[ListTaskResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTaskResponse` | `twilio_sdk/models/list_task_response.py` |

### client.taskrouter_v1_task.update_task

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def update_task(workspace_sid: str, sid: str, *, if_match: str | None = None, attributes: str | None = None, assignment_status: TaskEnumStatusOrStr | None = None, reason: str | None = None, priority: int | None = None, task_channel: str | None = None, virtual_start_time: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid` · `if_match` — header `If-Match` · `attributes` — form field `Attributes` · `assignment_status` — form field `AssignmentStatus` · `reason` — form field `Reason` · `priority` — form field `Priority` · `task_channel` — form field `TaskChannel` · `virtual_start_time` — form field `VirtualStartTime`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTask`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTask, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskEnumStatusOrStr` | `twilio_sdk/models/enums/task_enum_status.py` |
| `TaskrouterV1WorkspaceTask` | `twilio_sdk/models/taskrouter_v1_workspace_task.py` |

