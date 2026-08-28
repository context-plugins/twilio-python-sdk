<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1PortingPortInApi — operations

Accessor: `client.numbers_v1_porting_port_in_api` · Source: `twilio/apis/numbers_v1_porting_port_in_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v1_porting_port_in_api.create_porting_port_in

- **Route**: `POST /v1/Porting/PortIn`
- **Server**: `default5`
- **Signature**: `def create_porting_port_in(body: PortInRequest | PortInRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NumbersV1PortingPortIn`
- **Returns (raw)**: `ApiResult[NumbersV1PortingPortIn, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PortInRequest` | `twilio/models/port_in_request.py` |
| `PortInRequestDict` | `twilio/models/port_in_request.py` |
| `NumbersV1PortingPortIn` | `twilio/models/numbers_v1_porting_port_in.py` |

### client.numbers_v1_porting_port_in_api.delete_porting_port_in

- **Route**: `DELETE /v1/Porting/PortIn/{PortInRequestSid}`
- **Server**: `default5`
- **Signature**: `def delete_porting_port_in(port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `port_in_request_sid`
- **Params**: `port_in_request_sid` — path `PortInRequestSid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v1_porting_port_in_api.fetch_porting_port_in

- **Route**: `GET /v1/Porting/PortIn/{PortInRequestSid}`
- **Server**: `default5`
- **Signature**: `def fetch_porting_port_in(port_in_request_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `port_in_request_sid`
- **Params**: `port_in_request_sid` — path `PortInRequestSid`
- **Returns (parsed)**: `NumbersV1PortingPortIn`
- **Returns (raw)**: `ApiResult[NumbersV1PortingPortIn, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1PortingPortIn` | `twilio/models/numbers_v1_porting_port_in.py` |

### client.numbers_v1_porting_port_in_api.list_port_in_requests

- **Route**: `GET /v1/Porting/PortIn/PortInRequests`
- **Server**: `default5`
- **Signature**: `def list_port_in_requests(*, token: str | None = None, size: int | None = 20, port_in_request_sid: str | None = None, port_in_request_status: str | None = None, created_before: str | None = None, created_after: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `token` — query `Token` · `size` — query `Size` · `port_in_request_sid` — query `PortInRequestSid` · `port_in_request_status` — query `PortInRequestStatus` · `created_before` — query `CreatedBefore` · `created_after` — query `CreatedAfter`
- **Returns (parsed)**: `ListPortInRequestsResponse`
- **Returns (raw)**: `ApiResult[ListPortInRequestsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPortInRequestsResponse` | `twilio/models/list_port_in_requests_response.py` |

