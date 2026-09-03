<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1SyncMapPermission — operations

Accessor: `client.sync_v1_sync_map_permission` · Source: `twilio_sdk/apis/sync_v1_sync_map_permission.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.sync_v1_sync_map_permission.delete_sync_map_permission

- **Route**: `DELETE /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def delete_sync_map_permission(service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `identity` — path `Identity`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.sync_v1_sync_map_permission.fetch_sync_map_permission

- **Route**: `GET /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def fetch_sync_map_permission(service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `identity` — path `Identity`
- **Returns (parsed)**: `SyncV1ServiceSyncMapSyncMapPermission`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncMapSyncMapPermission, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncMapSyncMapPermission` | `twilio_sdk/models/sync_v1_service_sync_map_sync_map_permission.py` |

### client.sync_v1_sync_map_permission.list_sync_map_permission

- **Route**: `GET /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def list_sync_map_permission(service_sid: str, map_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSyncMapPermissionResponse`
- **Returns (raw)**: `ApiResult[ListSyncMapPermissionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSyncMapPermissionResponse` | `twilio_sdk/models/list_sync_map_permission_response.py` |

### client.sync_v1_sync_map_permission.update_sync_map_permission

- **Route**: `POST /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def update_sync_map_permission(service_sid: str, map_sid: str, identity: str, read: bool, write: bool, manage: bool, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`, `identity`, `read`, `write`, `manage`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `identity` — path `Identity` · `read` — form field `Read` · `write` — form field `Write` · `manage` — form field `Manage`
- **Returns (parsed)**: `SyncV1ServiceSyncMapSyncMapPermission`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncMapSyncMapPermission, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncMapSyncMapPermission` | `twilio_sdk/models/sync_v1_service_sync_map_sync_map_permission.py` |

