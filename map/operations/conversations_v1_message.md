<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1Message — operations

Accessor: `client.conversations_v1_message` · Source: `twilio/apis/conversations_v1_message.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_message.create_conversation_message

- **Route**: `POST /v1/Conversations/{ConversationSid}/Messages`
- **Server**: `default7`
- **Signature**: `def create_conversation_message(conversation_sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, author: str | None = None, body: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, media_sid: str | None = None, content_sid: str | None = None, content_variables: str | None = None, subject: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `author` — form field `Author` · `body` — form field `Body` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `media_sid` — form field `MediaSid` · `content_sid` — form field `ContentSid` · `content_variables` — form field `ContentVariables` · `subject` — form field `Subject`
- **Returns (parsed)**: `ConversationsV1ConversationConversationMessage`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1ConversationConversationMessage` | `twilio/models/conversations_v1_conversation_conversation_message.py` |

### client.conversations_v1_message.create_service_conversation_message

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages`
- **Server**: `default7`
- **Signature**: `def create_service_conversation_message(chat_service_sid: str, conversation_sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, author: str | None = None, body: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, media_sid: str | None = None, content_sid: str | None = None, content_variables: str | None = None, subject: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `author` — form field `Author` · `body` — form field `Body` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `media_sid` — form field `MediaSid` · `content_sid` — form field `ContentSid` · `content_variables` — form field `ContentVariables` · `subject` — form field `Subject`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationMessage`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1ServiceServiceConversationServiceConversationMessage` | `twilio/models/conversations_v1_service_service_conversation_service_conversation_message.py` |

### client.conversations_v1_message.delete_conversation_message

- **Route**: `DELETE /v1/Conversations/{ConversationSid}/Messages/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_conversation_message(conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |

### client.conversations_v1_message.delete_service_conversation_message

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_service_conversation_message(chat_service_sid: str, conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |

### client.conversations_v1_message.fetch_conversation_message

- **Route**: `GET /v1/Conversations/{ConversationSid}/Messages/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_conversation_message(conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ConversationConversationMessage`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ConversationConversationMessage` | `twilio/models/conversations_v1_conversation_conversation_message.py` |

### client.conversations_v1_message.fetch_service_conversation_message

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_service_conversation_message(chat_service_sid: str, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationMessage`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConversationServiceConversationMessage` | `twilio/models/conversations_v1_service_service_conversation_service_conversation_message.py` |

### client.conversations_v1_message.list_conversation_message

- **Route**: `GET /v1/Conversations/{ConversationSid}/Messages`
- **Server**: `default7`
- **Signature**: `def list_conversation_message(conversation_sid: str, *, order: ChallengeEnumListOrdersOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `order` — query `Order` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConversationMessageResponse`
- **Returns (raw)**: `ApiResult[ListConversationMessageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChallengeEnumListOrdersOrStr` | `twilio/models/enums/challenge_enum_list_orders.py` |
| `ListConversationMessageResponse` | `twilio/models/list_conversation_message_response.py` |

### client.conversations_v1_message.list_service_conversation_message

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages`
- **Server**: `default7`
- **Signature**: `def list_service_conversation_message(chat_service_sid: str, conversation_sid: str, *, order: ChallengeEnumListOrdersOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `order` — query `Order` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceConversationMessageResponse`
- **Returns (raw)**: `ApiResult[ListServiceConversationMessageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChallengeEnumListOrdersOrStr` | `twilio/models/enums/challenge_enum_list_orders.py` |
| `ListServiceConversationMessageResponse` | `twilio/models/list_service_conversation_message_response.py` |

### client.conversations_v1_message.update_conversation_message

- **Route**: `POST /v1/Conversations/{ConversationSid}/Messages/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_conversation_message(conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, author: str | None = None, body: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, subject: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `author` — form field `Author` · `body` — form field `Body` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `subject` — form field `Subject`
- **Returns (parsed)**: `ConversationsV1ConversationConversationMessage`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1ConversationConversationMessage` | `twilio/models/conversations_v1_conversation_conversation_message.py` |

### client.conversations_v1_message.update_service_conversation_message

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_service_conversation_message(chat_service_sid: str, conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, author: str | None = None, body: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, subject: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `author` — form field `Author` · `body` — form field `Body` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `subject` — form field `Subject`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationMessage`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio/models/enums/confirmation.py` |
| `ConversationsV1ServiceServiceConversationServiceConversationMessage` | `twilio/models/conversations_v1_service_service_conversation_service_conversation_message.py` |

