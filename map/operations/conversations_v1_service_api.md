<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1ServiceApi — operations

Accessor: `client.conversations_v1_service_api` · Source: `twilio_sdk/apis/conversations_v1_service_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.conversations_v1_service_api.create_service3

- **Route**: `POST /v1/Services`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_service3(friendly_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`
- **Params**: `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ConversationsV1Service`
- **Returns (raw)**: `ApiResult[ConversationsV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Service` | `twilio_sdk/models/conversations_v1_service.py` |

### client.conversations_v1_service_api.delete_service3

- **Route**: `DELETE /v1/Services/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def delete_service3(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_service_api.fetch_service3

- **Route**: `GET /v1/Services/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_service3(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1Service`
- **Returns (raw)**: `ApiResult[ConversationsV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Service` | `twilio_sdk/models/conversations_v1_service.py` |

### client.conversations_v1_service_api.list_service3

- **Route**: `GET /v1/Services`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_service3(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceResponse2`
- **Returns (raw)**: `ApiResult[ListServiceResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceResponse2` | `twilio_sdk/models/list_service_response2.py` |

