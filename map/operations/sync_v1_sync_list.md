<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1SyncList — operations

Accessor: `client.sync_v1_sync_list` · Source: `twilio_sdk/apis/sync_v1_sync_list.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.sync_v1_sync_list.create_sync_list

- **Route**: `POST /v1/Services/{ServiceSid}/Lists`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def create_sync_list(service_sid: str, *, unique_name: str | None = None, ttl: int | None = None, collection_ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `unique_name` — form field `UniqueName` · `ttl` — form field `Ttl` · `collection_ttl` — form field `CollectionTtl`
- **Returns (parsed)**: `SyncV1ServiceSyncList`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncList` | `twilio_sdk/models/sync_v1_service_sync_list.py` |

### client.sync_v1_sync_list.delete_sync_list

- **Route**: `DELETE /v1/Services/{ServiceSid}/Lists/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def delete_sync_list(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.sync_v1_sync_list.fetch_sync_list

- **Route**: `GET /v1/Services/{ServiceSid}/Lists/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def fetch_sync_list(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `SyncV1ServiceSyncList`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncList` | `twilio_sdk/models/sync_v1_service_sync_list.py` |

### client.sync_v1_sync_list.list_sync_list

- **Route**: `GET /v1/Services/{ServiceSid}/Lists`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def list_sync_list(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSyncListResponse`
- **Returns (raw)**: `ApiResult[ListSyncListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSyncListResponse` | `twilio_sdk/models/list_sync_list_response.py` |

### client.sync_v1_sync_list.update_sync_list

- **Route**: `POST /v1/Services/{ServiceSid}/Lists/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def update_sync_list(service_sid: str, sid: str, *, ttl: int | None = None, collection_ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid` · `ttl` — form field `Ttl` · `collection_ttl` — form field `CollectionTtl`
- **Returns (parsed)**: `SyncV1ServiceSyncList`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncList` | `twilio_sdk/models/sync_v1_service_sync_list.py` |

