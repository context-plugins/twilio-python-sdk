<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1RoleApi — operations

Accessor: `client.conversations_v1_role_api` · Source: `twilio/apis/conversations_v1_role_api.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.conversations_v1_role_api.create_role

- **Route**: `POST /v1/Roles`
- **Server**: `default7`
- **Signature**: `def create_role(friendly_name: str, type_: RoleEnumRoleTypeOrStr, permission: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `type_`, `permission`
- **Params**: `friendly_name` — form field `FriendlyName` · `type_` — form field `Type` · `permission` — form field `Permission`
- **Returns (parsed)**: `ConversationsV1Role`
- **Returns (raw)**: `ApiResult[ConversationsV1Role, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RoleEnumRoleTypeOrStr` | `twilio/models/enums/role_enum_role_type.py` |
| `ConversationsV1Role` | `twilio/models/conversations_v1_role.py` |

### client.conversations_v1_role_api.create_service_role

- **Route**: `POST /v1/Services/{ChatServiceSid}/Roles`
- **Server**: `default7`
- **Signature**: `def create_service_role(chat_service_sid: str, friendly_name: str, type_: ServiceRoleEnumRoleTypeOrStr, permission: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `friendly_name`, `type_`, `permission`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `friendly_name` — form field `FriendlyName` · `type_` — form field `Type` · `permission` — form field `Permission`
- **Returns (parsed)**: `ConversationsV1ServiceServiceRole`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceRole, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceRoleEnumRoleTypeOrStr` | `twilio/models/enums/service_role_enum_role_type.py` |
| `ConversationsV1ServiceServiceRole` | `twilio/models/conversations_v1_service_service_role.py` |

### client.conversations_v1_role_api.delete_role

- **Route**: `DELETE /v1/Roles/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_role(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_role_api.delete_service_role

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Roles/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_service_role(chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_role_api.fetch_role

- **Route**: `GET /v1/Roles/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_role(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1Role`
- **Returns (raw)**: `ApiResult[ConversationsV1Role, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Role` | `twilio/models/conversations_v1_role.py` |

### client.conversations_v1_role_api.fetch_service_role

- **Route**: `GET /v1/Services/{ChatServiceSid}/Roles/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_service_role(chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceRole`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceRole, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceRole` | `twilio/models/conversations_v1_service_service_role.py` |

### client.conversations_v1_role_api.list_role

- **Route**: `GET /v1/Roles`
- **Server**: `default7`
- **Signature**: `def list_role(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRoleResponse`
- **Returns (raw)**: `ApiResult[ListRoleResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRoleResponse` | `twilio/models/list_role_response.py` |

### client.conversations_v1_role_api.list_service_role

- **Route**: `GET /v1/Services/{ChatServiceSid}/Roles`
- **Server**: `default7`
- **Signature**: `def list_service_role(chat_service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceRoleResponse`
- **Returns (raw)**: `ApiResult[ListServiceRoleResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceRoleResponse` | `twilio/models/list_service_role_response.py` |

### client.conversations_v1_role_api.update_role

- **Route**: `POST /v1/Roles/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_role(sid: str, permission: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `permission`
- **Params**: `sid` — path `Sid` · `permission` — form field `Permission`
- **Returns (parsed)**: `ConversationsV1Role`
- **Returns (raw)**: `ApiResult[ConversationsV1Role, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Role` | `twilio/models/conversations_v1_role.py` |

### client.conversations_v1_role_api.update_service_role

- **Route**: `POST /v1/Services/{ChatServiceSid}/Roles/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_service_role(chat_service_sid: str, sid: str, permission: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`, `permission`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid` · `permission` — form field `Permission`
- **Returns (parsed)**: `ConversationsV1ServiceServiceRole`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceRole, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceRole` | `twilio/models/conversations_v1_service_service_role.py` |

