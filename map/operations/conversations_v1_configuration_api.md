<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1ConfigurationApi — operations

Accessor: `client.conversations_v1_configuration_api` · Source: `twilio_sdk/apis/conversations_v1_configuration_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_configuration_api.fetch_configuration

- **Route**: `GET /v1/Configuration`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_configuration(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ConversationsV1Configuration`
- **Returns (raw)**: `ApiResult[ConversationsV1Configuration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Configuration` | `twilio_sdk/models/conversations_v1_configuration.py` |

### client.conversations_v1_configuration_api.fetch_service_configuration

- **Route**: `GET /v1/Services/{ChatServiceSid}/Configuration`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_service_configuration(chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConfiguration`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConfiguration` | `twilio_sdk/models/conversations_v1_service_service_configuration.py` |

### client.conversations_v1_configuration_api.update_configuration

- **Route**: `POST /v1/Configuration`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_configuration(*, default_chat_service_sid: str | None = None, default_messaging_service_sid: str | None = None, default_inactive_timer: str | None = None, default_closed_timer: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `default_chat_service_sid` — form field `DefaultChatServiceSid` · `default_messaging_service_sid` — form field `DefaultMessagingServiceSid` · `default_inactive_timer` — form field `DefaultInactiveTimer` · `default_closed_timer` — form field `DefaultClosedTimer`
- **Returns (parsed)**: `ConversationsV1Configuration`
- **Returns (raw)**: `ApiResult[ConversationsV1Configuration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Configuration` | `twilio_sdk/models/conversations_v1_configuration.py` |

### client.conversations_v1_configuration_api.update_service_configuration

- **Route**: `POST /v1/Services/{ChatServiceSid}/Configuration`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_service_configuration(chat_service_sid: str, *, default_conversation_creator_role_sid: str | None = None, default_conversation_role_sid: str | None = None, default_chat_service_role_sid: str | None = None, reachability_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `default_conversation_creator_role_sid` — form field `DefaultConversationCreatorRoleSid` · `default_conversation_role_sid` — form field `DefaultConversationRoleSid` · `default_chat_service_role_sid` — form field `DefaultChatServiceRoleSid` · `reachability_enabled` — form field `ReachabilityEnabled`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConfiguration`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConfiguration` | `twilio_sdk/models/conversations_v1_service_service_configuration.py` |

