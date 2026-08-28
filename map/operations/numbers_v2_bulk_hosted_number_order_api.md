<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2BulkHostedNumberOrderApi — operations

Accessor: `client.numbers_v2_bulk_hosted_number_order_api` · Source: `twilio/apis/numbers_v2_bulk_hosted_number_order_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_bulk_hosted_number_order_api.create_bulk_hosted_number_order

- **Route**: `POST /v2/HostedNumber/Orders/Bulk`
- **Server**: `default5`
- **Signature**: `def create_bulk_hosted_number_order(*, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NumbersV2BulkHostedNumberOrder`
- **Returns (raw)**: `ApiResult[NumbersV2BulkHostedNumberOrder, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2BulkHostedNumberOrder` | `twilio/models/numbers_v2_bulk_hosted_number_order.py` |

### client.numbers_v2_bulk_hosted_number_order_api.fetch_bulk_hosted_number_order

- **Route**: `GET /v2/HostedNumber/Orders/Bulk/{BulkHostingSid}`
- **Server**: `default5`
- **Signature**: `def fetch_bulk_hosted_number_order(bulk_hosting_sid: str, *, order_status: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bulk_hosting_sid`
- **Params**: `bulk_hosting_sid` — path `BulkHostingSid` · `order_status` — query `OrderStatus`
- **Returns (parsed)**: `NumbersV2BulkHostedNumberOrder`
- **Returns (raw)**: `ApiResult[NumbersV2BulkHostedNumberOrder, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2BulkHostedNumberOrder` | `twilio/models/numbers_v2_bulk_hosted_number_order.py` |

