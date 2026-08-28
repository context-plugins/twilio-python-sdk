<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1SyncMapItem — operations

Accessor: `client.sync_v1_sync_map_item` · Source: `twilio_sdk/apis/sync_v1_sync_map_item.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.sync_v1_sync_map_item.create_sync_map_item

- **Route**: `POST /v1/Services/{ServiceSid}/Maps/{MapSid}/Items`
- **Server**: `default12`
- **Signature**: `def create_sync_map_item(service_sid: str, map_sid: str, key: str, data: Any, *, ttl: int | None = None, item_ttl: int | None = None, collection_ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`, `key`, `data`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `key` — form field `Key` · `data` — form field `Data` · `ttl` — form field `Ttl` · `item_ttl` — form field `ItemTtl` · `collection_ttl` — form field `CollectionTtl`
- **Returns (parsed)**: `SyncV1ServiceSyncMapSyncMapItem`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncMapSyncMapItem` | `twilio_sdk/models/sync_v1_service_sync_map_sync_map_item.py` |

### client.sync_v1_sync_map_item.delete_sync_map_item

- **Route**: `DELETE /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}`
- **Server**: `default12`
- **Signature**: `def delete_sync_map_item(service_sid: str, map_sid: str, key: str, *, if_match: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`, `key`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `key` — path `Key` · `if_match` — header `If-Match`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.sync_v1_sync_map_item.fetch_sync_map_item

- **Route**: `GET /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}`
- **Server**: `default12`
- **Signature**: `def fetch_sync_map_item(service_sid: str, map_sid: str, key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`, `key`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `key` — path `Key`
- **Returns (parsed)**: `SyncV1ServiceSyncMapSyncMapItem`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncMapSyncMapItem` | `twilio_sdk/models/sync_v1_service_sync_map_sync_map_item.py` |

### client.sync_v1_sync_map_item.list_sync_map_item

- **Route**: `GET /v1/Services/{ServiceSid}/Maps/{MapSid}/Items`
- **Server**: `default12`
- **Signature**: `def list_sync_map_item(service_sid: str, map_sid: str, *, order: ChallengeEnumListOrdersOrStr | None = None, from_: str | None = None, bounds: SyncMapItemEnumQueryFromBoundTypeOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `order` — query `Order` · `from_` — query `From` · `bounds` — query `Bounds` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSyncMapItemResponse`
- **Returns (raw)**: `ApiResult[ListSyncMapItemResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChallengeEnumListOrdersOrStr` | `twilio_sdk/models/enums/challenge_enum_list_orders.py` |
| `SyncMapItemEnumQueryFromBoundTypeOrStr` | `twilio_sdk/models/enums/sync_map_item_enum_query_from_bound_type.py` |
| `ListSyncMapItemResponse` | `twilio_sdk/models/list_sync_map_item_response.py` |

### client.sync_v1_sync_map_item.update_sync_map_item

- **Route**: `POST /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}`
- **Server**: `default12`
- **Signature**: `def update_sync_map_item(service_sid: str, map_sid: str, key: str, *, if_match: str | None = None, data: Any | None = None, ttl: int | None = None, item_ttl: int | None = None, collection_ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `map_sid`, `key`
- **Params**: `service_sid` — path `ServiceSid` · `map_sid` — path `MapSid` · `key` — path `Key` · `if_match` — header `If-Match` · `data` — form field `Data` · `ttl` — form field `Ttl` · `item_ttl` — form field `ItemTtl` · `collection_ttl` — form field `CollectionTtl`
- **Returns (parsed)**: `SyncV1ServiceSyncMapSyncMapItem`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncMapSyncMapItem` | `twilio_sdk/models/sync_v1_service_sync_map_sync_map_item.py` |

