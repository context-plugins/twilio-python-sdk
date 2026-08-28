<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1TaskChannel — operations

Accessor: `client.taskrouter_v1_task_channel` · Source: `twilio/apis/taskrouter_v1_task_channel.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.taskrouter_v1_task_channel.create_task_channel

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/TaskChannels`
- **Server**: `default8`
- **Signature**: `def create_task_channel(workspace_sid: str, friendly_name: str, unique_name: str, *, channel_optimized_routing: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `friendly_name`, `unique_name`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `friendly_name` — form field `FriendlyName` · `unique_name` — form field `UniqueName` · `channel_optimized_routing` — form field `ChannelOptimizedRouting`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTaskChannel`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTaskChannel` | `twilio/models/taskrouter_v1_workspace_task_channel.py` |

### client.taskrouter_v1_task_channel.delete_task_channel

- **Route**: `DELETE /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}`
- **Server**: `default8`
- **Signature**: `def delete_task_channel(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.taskrouter_v1_task_channel.fetch_task_channel

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}`
- **Server**: `default8`
- **Signature**: `def fetch_task_channel(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTaskChannel`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTaskChannel` | `twilio/models/taskrouter_v1_workspace_task_channel.py` |

### client.taskrouter_v1_task_channel.list_task_channel

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/TaskChannels`
- **Server**: `default8`
- **Signature**: `def list_task_channel(workspace_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTaskChannelResponse`
- **Returns (raw)**: `ApiResult[ListTaskChannelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTaskChannelResponse` | `twilio/models/list_task_channel_response.py` |

### client.taskrouter_v1_task_channel.update_task_channel

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}`
- **Server**: `default8`
- **Signature**: `def update_task_channel(workspace_sid: str, sid: str, *, friendly_name: str | None = None, channel_optimized_routing: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `channel_optimized_routing` — form field `ChannelOptimizedRouting`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTaskChannel`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTaskChannel` | `twilio/models/taskrouter_v1_workspace_task_channel.py` |

