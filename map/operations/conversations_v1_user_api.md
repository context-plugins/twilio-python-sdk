<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1UserApi — operations

Accessor: `client.conversations_v1_user_api` · Source: `twilio/apis/conversations_v1_user_api.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_user_api.create_service_user

- **Route**: `POST /v1/Services/{ChatServiceSid}/Users`
- **Server**: `default7`
- **Signature**: `def create_service_user(chat_service_sid: str, identity: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, attributes: str | None = None, role_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `identity`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `identity` — form field `Identity` · `friendly_name` — form field `FriendlyName` · `attributes` — form field `Attributes` · `role_sid` — form field `RoleSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceUser`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1ServiceServiceUser` | `twilio/models/conversations_v1_service_service_user.py` |

### client.conversations_v1_user_api.create_user

- **Route**: `POST /v1/Users`
- **Server**: `default7`
- **Signature**: `def create_user(identity: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, attributes: str | None = None, role_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `identity`
- **Params**: `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `identity` — form field `Identity` · `friendly_name` — form field `FriendlyName` · `attributes` — form field `Attributes` · `role_sid` — form field `RoleSid`
- **Returns (parsed)**: `ConversationsV1User`
- **Returns (raw)**: `ApiResult[ConversationsV1User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1User` | `twilio/models/conversations_v1_user.py` |

### client.conversations_v1_user_api.delete_service_user

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Users/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_service_user(chat_service_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |

### client.conversations_v1_user_api.delete_user

- **Route**: `DELETE /v1/Users/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_user(sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |

### client.conversations_v1_user_api.fetch_service_user

- **Route**: `GET /v1/Services/{ChatServiceSid}/Users/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_service_user(chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceUser`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceUser` | `twilio/models/conversations_v1_service_service_user.py` |

### client.conversations_v1_user_api.fetch_user

- **Route**: `GET /v1/Users/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_user(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1User`
- **Returns (raw)**: `ApiResult[ConversationsV1User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1User` | `twilio/models/conversations_v1_user.py` |

### client.conversations_v1_user_api.list_service_user

- **Route**: `GET /v1/Services/{ChatServiceSid}/Users`
- **Server**: `default7`
- **Signature**: `def list_service_user(chat_service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceUserResponse`
- **Returns (raw)**: `ApiResult[ListServiceUserResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceUserResponse` | `twilio/models/list_service_user_response.py` |

### client.conversations_v1_user_api.list_user

- **Route**: `GET /v1/Users`
- **Server**: `default7`
- **Signature**: `def list_user(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListUserResponse`
- **Returns (raw)**: `ApiResult[ListUserResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListUserResponse` | `twilio/models/list_user_response.py` |

### client.conversations_v1_user_api.update_service_user

- **Route**: `POST /v1/Services/{ChatServiceSid}/Users/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_service_user(chat_service_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, attributes: str | None = None, role_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `attributes` — form field `Attributes` · `role_sid` — form field `RoleSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceUser`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1ServiceServiceUser` | `twilio/models/conversations_v1_service_service_user.py` |

### client.conversations_v1_user_api.update_user

- **Route**: `POST /v1/Users/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_user(sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, attributes: str | None = None, role_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `attributes` — form field `Attributes` · `role_sid` — form field `RoleSid`
- **Returns (parsed)**: `ConversationsV1User`
- **Returns (raw)**: `ApiResult[ConversationsV1User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1User` | `twilio/models/conversations_v1_user.py` |

