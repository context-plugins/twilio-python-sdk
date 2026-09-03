<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1WorkspaceApi — operations

Accessor: `client.taskrouter_v1_workspace_api` · Source: `twilio_sdk/apis/taskrouter_v1_workspace_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.taskrouter_v1_workspace_api.create_workspace

- **Route**: `POST /v1/Workspaces`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def create_workspace(friendly_name: str, *, event_callback_url: str | None = None, events_filter: str | None = None, multi_task_enabled: bool | None = None, template: str | None = None, prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`
- **Params**: `friendly_name` — form field `FriendlyName` · `event_callback_url` — form field `EventCallbackUrl` · `events_filter` — form field `EventsFilter` · `multi_task_enabled` — form field `MultiTaskEnabled` · `template` — form field `Template` · `prioritize_queue_order` — form field `PrioritizeQueueOrder`
- **Returns (parsed)**: `TaskrouterV1Workspace`
- **Returns (raw)**: `ApiResult[TaskrouterV1Workspace, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WorkspaceEnumQueueOrderOrStr` | `twilio_sdk/models/enums/workspace_enum_queue_order.py` |
| `TaskrouterV1Workspace` | `twilio_sdk/models/taskrouter_v1_workspace.py` |

### client.taskrouter_v1_workspace_api.delete_workspace

- **Route**: `DELETE /v1/Workspaces/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def delete_workspace(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.taskrouter_v1_workspace_api.fetch_workspace

- **Route**: `GET /v1/Workspaces/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def fetch_workspace(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1Workspace`
- **Returns (raw)**: `ApiResult[TaskrouterV1Workspace, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1Workspace` | `twilio_sdk/models/taskrouter_v1_workspace.py` |

### client.taskrouter_v1_workspace_api.list_workspace

- **Route**: `GET /v1/Workspaces`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def list_workspace(*, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListWorkspaceResponse`
- **Returns (raw)**: `ApiResult[ListWorkspaceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWorkspaceResponse` | `twilio_sdk/models/list_workspace_response.py` |

### client.taskrouter_v1_workspace_api.update_workspace

- **Route**: `POST /v1/Workspaces/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def update_workspace(sid: str, *, default_activity_sid: str | None = None, event_callback_url: str | None = None, events_filter: str | None = None, friendly_name: str | None = None, multi_task_enabled: bool | None = None, timeout_activity_sid: str | None = None, prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `default_activity_sid` — form field `DefaultActivitySid` · `event_callback_url` — form field `EventCallbackUrl` · `events_filter` — form field `EventsFilter` · `friendly_name` — form field `FriendlyName` · `multi_task_enabled` — form field `MultiTaskEnabled` · `timeout_activity_sid` — form field `TimeoutActivitySid` · `prioritize_queue_order` — form field `PrioritizeQueueOrder`
- **Returns (parsed)**: `TaskrouterV1Workspace`
- **Returns (raw)**: `ApiResult[TaskrouterV1Workspace, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WorkspaceEnumQueueOrderOrStr` | `twilio_sdk/models/enums/workspace_enum_queue_order.py` |
| `TaskrouterV1Workspace` | `twilio_sdk/models/taskrouter_v1_workspace.py` |

