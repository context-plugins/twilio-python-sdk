<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1WorkerChannel — operations

Accessor: `client.taskrouter_v1_worker_channel` · Source: `twilio_sdk/apis/taskrouter_v1_worker_channel.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_worker_channel.fetch_worker_channel

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid}`
- **Server**: `default8`
- **Signature**: `def fetch_worker_channel(workspace_sid: str, worker_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `worker_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `worker_sid` — path `WorkerSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorkerWorkerChannel`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorkerWorkerChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorkerWorkerChannel` | `twilio_sdk/models/taskrouter_v1_workspace_worker_worker_channel.py` |

### client.taskrouter_v1_worker_channel.list_worker_channel

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels`
- **Server**: `default8`
- **Signature**: `def list_worker_channel(workspace_sid: str, worker_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `worker_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `worker_sid` — path `WorkerSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListWorkerChannelResponse`
- **Returns (raw)**: `ApiResult[ListWorkerChannelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWorkerChannelResponse` | `twilio_sdk/models/list_worker_channel_response.py` |

### client.taskrouter_v1_worker_channel.update_worker_channel

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid}`
- **Server**: `default8`
- **Signature**: `def update_worker_channel(workspace_sid: str, worker_sid: str, sid: str, *, capacity: int | None = None, available: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `worker_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `worker_sid` — path `WorkerSid` · `sid` — path `Sid` · `capacity` — form field `Capacity` · `available` — form field `Available`
- **Returns (parsed)**: `TaskrouterV1WorkspaceWorkerWorkerChannel`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceWorkerWorkerChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceWorkerWorkerChannel` | `twilio_sdk/models/taskrouter_v1_workspace_worker_worker_channel.py` |

