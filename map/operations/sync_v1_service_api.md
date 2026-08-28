<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1ServiceApi — operations

Accessor: `client.sync_v1_service_api` · Source: `twilio/apis/sync_v1_service_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.sync_v1_service_api.create_service5

- **Route**: `POST /v1/Services`
- **Server**: `default12`
- **Signature**: `def create_service5(*, friendly_name: str | None = None, webhook_url: str | None = None, reachability_webhooks_enabled: bool | None = None, acl_enabled: bool | None = None, reachability_debouncing_enabled: bool | None = None, reachability_debouncing_window: int | None = None, webhooks_from_rest_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `friendly_name` — form field `FriendlyName` · `webhook_url` — form field `WebhookUrl` · `reachability_webhooks_enabled` — form field `ReachabilityWebhooksEnabled` · `acl_enabled` — form field `AclEnabled` · `reachability_debouncing_enabled` — form field `ReachabilityDebouncingEnabled` · `reachability_debouncing_window` — form field `ReachabilityDebouncingWindow` · `webhooks_from_rest_enabled` — form field `WebhooksFromRestEnabled`
- **Returns (parsed)**: `SyncV1Service`
- **Returns (raw)**: `ApiResult[SyncV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1Service` | `twilio/models/sync_v1_service.py` |

### client.sync_v1_service_api.delete_service5

- **Route**: `DELETE /v1/Services/{Sid}`
- **Server**: `default12`
- **Signature**: `def delete_service5(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.sync_v1_service_api.fetch_service5

- **Route**: `GET /v1/Services/{Sid}`
- **Server**: `default12`
- **Signature**: `def fetch_service5(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `SyncV1Service`
- **Returns (raw)**: `ApiResult[SyncV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1Service` | `twilio/models/sync_v1_service.py` |

### client.sync_v1_service_api.list_service5

- **Route**: `GET /v1/Services`
- **Server**: `default12`
- **Signature**: `def list_service5(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceResponse4`
- **Returns (raw)**: `ApiResult[ListServiceResponse4, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceResponse4` | `twilio/models/list_service_response4.py` |

### client.sync_v1_service_api.update_service4

- **Route**: `POST /v1/Services/{Sid}`
- **Server**: `default12`
- **Signature**: `def update_service4(sid: str, *, webhook_url: str | None = None, friendly_name: str | None = None, reachability_webhooks_enabled: bool | None = None, acl_enabled: bool | None = None, reachability_debouncing_enabled: bool | None = None, reachability_debouncing_window: int | None = None, webhooks_from_rest_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `webhook_url` — form field `WebhookUrl` · `friendly_name` — form field `FriendlyName` · `reachability_webhooks_enabled` — form field `ReachabilityWebhooksEnabled` · `acl_enabled` — form field `AclEnabled` · `reachability_debouncing_enabled` — form field `ReachabilityDebouncingEnabled` · `reachability_debouncing_window` — form field `ReachabilityDebouncingWindow` · `webhooks_from_rest_enabled` — form field `WebhooksFromRestEnabled`
- **Returns (parsed)**: `SyncV1Service`
- **Returns (raw)**: `ApiResult[SyncV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1Service` | `twilio/models/sync_v1_service.py` |

