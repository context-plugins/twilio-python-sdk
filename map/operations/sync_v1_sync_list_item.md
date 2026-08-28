<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1SyncListItem — operations

Accessor: `client.sync_v1_sync_list_item` · Source: `twilio/apis/sync_v1_sync_list_item.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.sync_v1_sync_list_item.create_sync_list_item

- **Route**: `POST /v1/Services/{ServiceSid}/Lists/{ListSid}/Items`
- **Server**: `default12`
- **Signature**: `def create_sync_list_item(service_sid: str, list_sid: str, data: Any, *, ttl: int | None = None, item_ttl: int | None = None, collection_ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `list_sid`, `data`
- **Params**: `service_sid` — path `ServiceSid` · `list_sid` — path `ListSid` · `data` — form field `Data` · `ttl` — form field `Ttl` · `item_ttl` — form field `ItemTtl` · `collection_ttl` — form field `CollectionTtl`
- **Returns (parsed)**: `SyncV1ServiceSyncListSyncListItem`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncListSyncListItem` | `twilio/models/sync_v1_service_sync_list_sync_list_item.py` |

### client.sync_v1_sync_list_item.delete_sync_list_item

- **Route**: `DELETE /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}`
- **Server**: `default12`
- **Signature**: `def delete_sync_list_item(service_sid: str, list_sid: str, index: int, *, if_match: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `list_sid`, `index`
- **Params**: `service_sid` — path `ServiceSid` · `list_sid` — path `ListSid` · `index` — path `Index` · `if_match` — header `If-Match`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.sync_v1_sync_list_item.fetch_sync_list_item

- **Route**: `GET /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}`
- **Server**: `default12`
- **Signature**: `def fetch_sync_list_item(service_sid: str, list_sid: str, index: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `list_sid`, `index`
- **Params**: `service_sid` — path `ServiceSid` · `list_sid` — path `ListSid` · `index` — path `Index`
- **Returns (parsed)**: `SyncV1ServiceSyncListSyncListItem`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncListSyncListItem` | `twilio/models/sync_v1_service_sync_list_sync_list_item.py` |

### client.sync_v1_sync_list_item.list_sync_list_item

- **Route**: `GET /v1/Services/{ServiceSid}/Lists/{ListSid}/Items`
- **Server**: `default12`
- **Signature**: `def list_sync_list_item(service_sid: str, list_sid: str, *, order: ChallengeEnumListOrdersOrStr | None = None, from_: str | None = None, bounds: SyncListItemEnumQueryFromBoundTypeOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `list_sid`
- **Params**: `service_sid` — path `ServiceSid` · `list_sid` — path `ListSid` · `order` — query `Order` · `from_` — query `From` · `bounds` — query `Bounds` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSyncListItemResponse`
- **Returns (raw)**: `ApiResult[ListSyncListItemResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChallengeEnumListOrdersOrStr` | `twilio/models/enums/challenge_enum_list_orders.py` |
| `SyncListItemEnumQueryFromBoundTypeOrStr` | `twilio/models/enums/sync_list_item_enum_query_from_bound_type.py` |
| `ListSyncListItemResponse` | `twilio/models/list_sync_list_item_response.py` |

### client.sync_v1_sync_list_item.update_sync_list_item

- **Route**: `POST /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}`
- **Server**: `default12`
- **Signature**: `def update_sync_list_item(service_sid: str, list_sid: str, index: int, *, if_match: str | None = None, data: Any | None = None, ttl: int | None = None, item_ttl: int | None = None, collection_ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `list_sid`, `index`
- **Params**: `service_sid` — path `ServiceSid` · `list_sid` — path `ListSid` · `index` — path `Index` · `if_match` — header `If-Match` · `data` — form field `Data` · `ttl` — form field `Ttl` · `item_ttl` — form field `ItemTtl` · `collection_ttl` — form field `CollectionTtl`
- **Returns (parsed)**: `SyncV1ServiceSyncListSyncListItem`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncListSyncListItem` | `twilio/models/sync_v1_service_sync_list_sync_list_item.py` |

