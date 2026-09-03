<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1ConversationApi — operations

Accessor: `client.conversations_v1_conversation_api` · Source: `twilio_sdk/apis/conversations_v1_conversation_api.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_conversation_api.create_conversation

- **Route**: `POST /v1/Conversations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_conversation(*, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, unique_name: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, messaging_service_sid: str | None = None, attributes: str | None = None, state: ConversationEnumStateOrStr | None = None, timers_inactive: str | None = None, timers_closed: str | None = None, bindings_email_address: str | None = None, bindings_email_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `unique_name` — form field `UniqueName` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `messaging_service_sid` — form field `MessagingServiceSid` · `attributes` — form field `Attributes` · `state` — form field `State` · `timers_inactive` — form field `Timers.Inactive` · `timers_closed` — form field `Timers.Closed` · `bindings_email_address` — form field `Bindings.Email.Address` · `bindings_email_name` — form field `Bindings.Email.Name`
- **Returns (parsed)**: `ConversationsV1Conversation`
- **Returns (raw)**: `ApiResult[ConversationsV1Conversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ConversationEnumStateOrStr` | `twilio_sdk/models/enums/conversation_enum_state.py` |
| `ConversationsV1Conversation` | `twilio_sdk/models/conversations_v1_conversation.py` |

### client.conversations_v1_conversation_api.create_service_conversation

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_service_conversation(chat_service_sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, unique_name: str | None = None, attributes: str | None = None, messaging_service_sid: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, state: ServiceConversationEnumStateOrStr | None = None, timers_inactive: str | None = None, timers_closed: str | None = None, bindings_email_address: str | None = None, bindings_email_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `unique_name` — form field `UniqueName` · `attributes` — form field `Attributes` · `messaging_service_sid` — form field `MessagingServiceSid` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `state` — form field `State` · `timers_inactive` — form field `Timers.Inactive` · `timers_closed` — form field `Timers.Closed` · `bindings_email_address` — form field `Bindings.Email.Address` · `bindings_email_name` — form field `Bindings.Email.Name`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversation`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ServiceConversationEnumStateOrStr` | `twilio_sdk/models/enums/service_conversation_enum_state.py` |
| `ConversationsV1ServiceServiceConversation` | `twilio_sdk/models/conversations_v1_service_service_conversation.py` |

### client.conversations_v1_conversation_api.delete_conversation

- **Route**: `DELETE /v1/Conversations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def delete_conversation(sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |

### client.conversations_v1_conversation_api.delete_service_conversation

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Conversations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def delete_service_conversation(chat_service_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |

### client.conversations_v1_conversation_api.fetch_conversation

- **Route**: `GET /v1/Conversations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_conversation(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1Conversation`
- **Returns (raw)**: `ApiResult[ConversationsV1Conversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Conversation` | `twilio_sdk/models/conversations_v1_conversation.py` |

### client.conversations_v1_conversation_api.fetch_service_conversation

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_service_conversation(chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversation`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConversation` | `twilio_sdk/models/conversations_v1_service_service_conversation.py` |

### client.conversations_v1_conversation_api.list_conversation

- **Route**: `GET /v1/Conversations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_conversation(*, start_date: str | None = None, end_date: str | None = None, state: ConversationEnumStateOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `start_date` — query `StartDate` · `end_date` — query `EndDate` · `state` — query `State` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConversationResponse`
- **Returns (raw)**: `ApiResult[ListConversationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationEnumStateOrStr` | `twilio_sdk/models/enums/conversation_enum_state.py` |
| `ListConversationResponse` | `twilio_sdk/models/list_conversation_response.py` |

### client.conversations_v1_conversation_api.list_service_conversation

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_service_conversation(chat_service_sid: str, *, start_date: str | None = None, end_date: str | None = None, state: ServiceConversationEnumStateOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `start_date` — query `StartDate` · `end_date` — query `EndDate` · `state` — query `State` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceConversationResponse`
- **Returns (raw)**: `ApiResult[ListServiceConversationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceConversationEnumStateOrStr` | `twilio_sdk/models/enums/service_conversation_enum_state.py` |
| `ListServiceConversationResponse` | `twilio_sdk/models/list_service_conversation_response.py` |

### client.conversations_v1_conversation_api.update_conversation

- **Route**: `POST /v1/Conversations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_conversation(sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, messaging_service_sid: str | None = None, state: ConversationEnumStateOrStr | None = None, timers_inactive: str | None = None, timers_closed: str | None = None, unique_name: str | None = None, bindings_email_address: str | None = None, bindings_email_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `messaging_service_sid` — form field `MessagingServiceSid` · `state` — form field `State` · `timers_inactive` — form field `Timers.Inactive` · `timers_closed` — form field `Timers.Closed` · `unique_name` — form field `UniqueName` · `bindings_email_address` — form field `Bindings.Email.Address` · `bindings_email_name` — form field `Bindings.Email.Name`
- **Returns (parsed)**: `ConversationsV1Conversation`
- **Returns (raw)**: `ApiResult[ConversationsV1Conversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ConversationEnumStateOrStr` | `twilio_sdk/models/enums/conversation_enum_state.py` |
| `ConversationsV1Conversation` | `twilio_sdk/models/conversations_v1_conversation.py` |

### client.conversations_v1_conversation_api.update_service_conversation

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_service_conversation(chat_service_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, messaging_service_sid: str | None = None, state: ServiceConversationEnumStateOrStr | None = None, timers_inactive: str | None = None, timers_closed: str | None = None, unique_name: str | None = None, bindings_email_address: str | None = None, bindings_email_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `messaging_service_sid` — form field `MessagingServiceSid` · `state` — form field `State` · `timers_inactive` — form field `Timers.Inactive` · `timers_closed` — form field `Timers.Closed` · `unique_name` — form field `UniqueName` · `bindings_email_address` — form field `Bindings.Email.Address` · `bindings_email_name` — form field `Bindings.Email.Name`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversation`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ServiceConversationEnumStateOrStr` | `twilio_sdk/models/enums/service_conversation_enum_state.py` |
| `ConversationsV1ServiceServiceConversation` | `twilio_sdk/models/conversations_v1_service_service_conversation.py` |

