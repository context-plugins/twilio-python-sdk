<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1Binding — operations

Accessor: `client.conversations_v1_binding` · Source: `twilio_sdk/apis/conversations_v1_binding.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.conversations_v1_binding.delete_service_binding

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Bindings/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_service_binding(chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_binding.fetch_service_binding

- **Route**: `GET /v1/Services/{ChatServiceSid}/Bindings/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_service_binding(chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceBinding`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceBinding, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceBinding` | `twilio_sdk/models/conversations_v1_service_service_binding.py` |

### client.conversations_v1_binding.list_service_binding

- **Route**: `GET /v1/Services/{ChatServiceSid}/Bindings`
- **Server**: `default7`
- **Signature**: `def list_service_binding(chat_service_sid: str, *, binding_type: list[ServiceBindingEnumBindingTypeOrStr] | None = None, identity: list[str] | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `binding_type` — query `BindingType` · `identity` — query `Identity` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceBindingResponse`
- **Returns (raw)**: `ApiResult[ListServiceBindingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceBindingEnumBindingTypeOrStr` | `twilio_sdk/models/enums/service_binding_enum_binding_type.py` |
| `ListServiceBindingResponse` | `twilio_sdk/models/list_service_binding_response.py` |

