<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1Workflow — operations

Accessor: `client.taskrouter_v1_workflow` · Source: `twilio_sdk/apis/taskrouter_v1_workflow.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.taskrouter_v1_workflow.create_workflow

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Workflows`
- **Server**: `default8`
- **Signature**: `def create_workflow(workspace_sid: str, friendly_name: str, configuration: str, *, assignment_callback_url: AnyUrl | None = None, fallback_assignment_callback_url: AnyUrl | None = None, task_reservation_timeout: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `friendly_name`, `configuration`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `friendly_name` — form field `FriendlyName` · `configuration` — form field `Configuration` · `assignment_callback_url` — form field `AssignmentCallbackUrl` · `fallback_assignment_callback_url` — form field `FallbackAssignmentCallbackUrl` · `task_reservation_timeout` — form field `TaskReservationTimeout`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorkflow`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorkflow` | `twilio_sdk/models/taskrouter_v1_workspace_workflow.py` |

### client.taskrouter_v1_workflow.delete_workflow

- **Route**: `DELETE /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}`
- **Server**: `default8`
- **Signature**: `def delete_workflow(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.taskrouter_v1_workflow.fetch_workflow

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}`
- **Server**: `default8`
- **Signature**: `def fetch_workflow(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorkflow`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorkflow` | `twilio_sdk/models/taskrouter_v1_workspace_workflow.py` |

### client.taskrouter_v1_workflow.list_workflow

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workflows`
- **Server**: `default8`
- **Signature**: `def list_workflow(workspace_sid: str, *, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListWorkflowResponse`
- **Returns (raw)**: `ApiResult[ListWorkflowResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWorkflowResponse` | `twilio_sdk/models/list_workflow_response.py` |

### client.taskrouter_v1_workflow.update_workflow

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}`
- **Server**: `default8`
- **Signature**: `def update_workflow(workspace_sid: str, sid: str, *, friendly_name: str | None = None, assignment_callback_url: AnyUrl | None = None, fallback_assignment_callback_url: AnyUrl | None = None, configuration: str | None = None, task_reservation_timeout: int | None = None, re_evaluate_tasks: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `assignment_callback_url` — form field `AssignmentCallbackUrl` · `fallback_assignment_callback_url` — form field `FallbackAssignmentCallbackUrl` · `configuration` — form field `Configuration` · `task_reservation_timeout` — form field `TaskReservationTimeout` · `re_evaluate_tasks` — form field `ReEvaluateTasks`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorkflow`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorkflow` | `twilio_sdk/models/taskrouter_v1_workspace_workflow.py` |

