<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1Activity — operations

Accessor: `client.taskrouter_v1_activity` · Source: `twilio_sdk/apis/taskrouter_v1_activity.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.taskrouter_v1_activity.create_activity

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Activities`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def create_activity(workspace_sid: str, friendly_name: str, *, available: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `friendly_name`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `friendly_name` — form field `FriendlyName` · `available` — form field `Available`
- **Returns (parsed)**: `TaskrouterV1WorkspaceActivity`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceActivity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceActivity` | `twilio_sdk/models/taskrouter_v1_workspace_activity.py` |

### client.taskrouter_v1_activity.delete_activity

- **Route**: `DELETE /v1/Workspaces/{WorkspaceSid}/Activities/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def delete_activity(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.taskrouter_v1_activity.fetch_activity

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Activities/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def fetch_activity(workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceActivity`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceActivity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceActivity` | `twilio_sdk/models/taskrouter_v1_workspace_activity.py` |

### client.taskrouter_v1_activity.list_activity

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Activities`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def list_activity(workspace_sid: str, *, friendly_name: str | None = None, available: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `friendly_name` — query `FriendlyName` · `available` — query `Available` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListActivityResponse`
- **Returns (raw)**: `ApiResult[ListActivityResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListActivityResponse` | `twilio_sdk/models/list_activity_response.py` |

### client.taskrouter_v1_activity.update_activity

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Activities/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default8`
- **Signature**: `def update_activity(workspace_sid: str, sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `TaskrouterV1WorkspaceActivity`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceActivity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceActivity` | `twilio_sdk/models/taskrouter_v1_workspace_activity.py` |

