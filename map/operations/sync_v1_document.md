<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1Document — operations

Accessor: `client.sync_v1_document` · Source: `twilio_sdk/apis/sync_v1_document.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.sync_v1_document.create_document

- **Route**: `POST /v1/Services/{ServiceSid}/Documents`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def create_document(service_sid: str, *, unique_name: str | None = None, data: Any | None = None, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `unique_name` — form field `UniqueName` · `data` — form field `Data` · `ttl` — form field `Ttl`
- **Returns (parsed)**: `SyncV1ServiceDocument`
- **Returns (raw)**: `ApiResult[SyncV1ServiceDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceDocument` | `twilio_sdk/models/sync_v1_service_document.py` |

### client.sync_v1_document.delete_document

- **Route**: `DELETE /v1/Services/{ServiceSid}/Documents/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def delete_document(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.sync_v1_document.fetch_document

- **Route**: `GET /v1/Services/{ServiceSid}/Documents/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def fetch_document(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `SyncV1ServiceDocument`
- **Returns (raw)**: `ApiResult[SyncV1ServiceDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceDocument` | `twilio_sdk/models/sync_v1_service_document.py` |

### client.sync_v1_document.list_document

- **Route**: `GET /v1/Services/{ServiceSid}/Documents`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def list_document(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListDocumentResponse`
- **Returns (raw)**: `ApiResult[ListDocumentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListDocumentResponse` | `twilio_sdk/models/list_document_response.py` |

### client.sync_v1_document.update_document

- **Route**: `POST /v1/Services/{ServiceSid}/Documents/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def update_document(service_sid: str, sid: str, *, if_match: str | None = None, data: Any | None = None, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid` · `if_match` — header `If-Match` · `data` — form field `Data` · `ttl` — form field `Ttl`
- **Returns (parsed)**: `SyncV1ServiceDocument`
- **Returns (raw)**: `ApiResult[SyncV1ServiceDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceDocument` | `twilio_sdk/models/sync_v1_service_document.py` |

