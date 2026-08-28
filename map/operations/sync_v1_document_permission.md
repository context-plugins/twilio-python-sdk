<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1DocumentPermission — operations

Accessor: `client.sync_v1_document_permission` · Source: `twilio_sdk/apis/sync_v1_document_permission.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.sync_v1_document_permission.delete_document_permission

- **Route**: `DELETE /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}`
- **Server**: `default12`
- **Signature**: `def delete_document_permission(service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `document_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `document_sid` — path `DocumentSid` · `identity` — path `Identity`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.sync_v1_document_permission.fetch_document_permission

- **Route**: `GET /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}`
- **Server**: `default12`
- **Signature**: `def fetch_document_permission(service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `document_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `document_sid` — path `DocumentSid` · `identity` — path `Identity`
- **Returns (parsed)**: `SyncV1ServiceDocumentDocumentPermission`
- **Returns (raw)**: `ApiResult[SyncV1ServiceDocumentDocumentPermission, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceDocumentDocumentPermission` | `twilio_sdk/models/sync_v1_service_document_document_permission.py` |

### client.sync_v1_document_permission.list_document_permission

- **Route**: `GET /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions`
- **Server**: `default12`
- **Signature**: `def list_document_permission(service_sid: str, document_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `document_sid`
- **Params**: `service_sid` — path `ServiceSid` · `document_sid` — path `DocumentSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListDocumentPermissionResponse`
- **Returns (raw)**: `ApiResult[ListDocumentPermissionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListDocumentPermissionResponse` | `twilio_sdk/models/list_document_permission_response.py` |

### client.sync_v1_document_permission.update_document_permission

- **Route**: `POST /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}`
- **Server**: `default12`
- **Signature**: `def update_document_permission(service_sid: str, document_sid: str, identity: str, read: bool, write: bool, manage: bool, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `document_sid`, `identity`, `read`, `write`, `manage`
- **Params**: `service_sid` — path `ServiceSid` · `document_sid` — path `DocumentSid` · `identity` — path `Identity` · `read` — form field `Read` · `write` — form field `Write` · `manage` — form field `Manage`
- **Returns (parsed)**: `SyncV1ServiceDocumentDocumentPermission`
- **Returns (raw)**: `ApiResult[SyncV1ServiceDocumentDocumentPermission, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceDocumentDocumentPermission` | `twilio_sdk/models/sync_v1_service_document_document_permission.py` |

