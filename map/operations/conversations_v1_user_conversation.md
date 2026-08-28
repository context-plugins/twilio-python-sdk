<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1UserConversation — operations

Accessor: `client.conversations_v1_user_conversation` · Source: `twilio/apis/conversations_v1_user_conversation.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.conversations_v1_user_conversation.delete_service_user_conversation

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}`
- **Server**: `default7`
- **Signature**: `def delete_service_user_conversation(chat_service_sid: str, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `user_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `user_sid` — path `UserSid` · `conversation_sid` — path `ConversationSid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_user_conversation.delete_user_conversation

- **Route**: `DELETE /v1/Users/{UserSid}/Conversations/{ConversationSid}`
- **Server**: `default7`
- **Signature**: `def delete_user_conversation(user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_sid`, `conversation_sid`
- **Params**: `user_sid` — path `UserSid` · `conversation_sid` — path `ConversationSid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_user_conversation.fetch_service_user_conversation

- **Route**: `GET /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}`
- **Server**: `default7`
- **Signature**: `def fetch_service_user_conversation(chat_service_sid: str, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `user_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `user_sid` — path `UserSid` · `conversation_sid` — path `ConversationSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceUserServiceUserConversation`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceUserServiceUserConversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceUserServiceUserConversation` | `twilio/models/conversations_v1_service_service_user_service_user_conversation.py` |

### client.conversations_v1_user_conversation.fetch_user_conversation

- **Route**: `GET /v1/Users/{UserSid}/Conversations/{ConversationSid}`
- **Server**: `default7`
- **Signature**: `def fetch_user_conversation(user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_sid`, `conversation_sid`
- **Params**: `user_sid` — path `UserSid` · `conversation_sid` — path `ConversationSid`
- **Returns (parsed)**: `ConversationsV1UserUserConversation`
- **Returns (raw)**: `ApiResult[ConversationsV1UserUserConversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1UserUserConversation` | `twilio/models/conversations_v1_user_user_conversation.py` |

### client.conversations_v1_user_conversation.list_service_user_conversation

- **Route**: `GET /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations`
- **Server**: `default7`
- **Signature**: `def list_service_user_conversation(chat_service_sid: str, user_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `user_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `user_sid` — path `UserSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceUserConversationResponse`
- **Returns (raw)**: `ApiResult[ListServiceUserConversationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceUserConversationResponse` | `twilio/models/list_service_user_conversation_response.py` |

### client.conversations_v1_user_conversation.list_user_conversation

- **Route**: `GET /v1/Users/{UserSid}/Conversations`
- **Server**: `default7`
- **Signature**: `def list_user_conversation(user_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_sid`
- **Params**: `user_sid` — path `UserSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListUserConversationResponse`
- **Returns (raw)**: `ApiResult[ListUserConversationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListUserConversationResponse` | `twilio/models/list_user_conversation_response.py` |

### client.conversations_v1_user_conversation.update_service_user_conversation

- **Route**: `POST /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}`
- **Server**: `default7`
- **Signature**: `def update_service_user_conversation(chat_service_sid: str, user_sid: str, conversation_sid: str, *, notification_level: ServiceUserConversationEnumNotificationLevelOrStr | None = None, last_read_timestamp: RFC3339DateTime | None = None, last_read_message_index: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `user_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `user_sid` — path `UserSid` · `conversation_sid` — path `ConversationSid` · `notification_level` — form field `NotificationLevel` · `last_read_timestamp` — form field `LastReadTimestamp` · `last_read_message_index` — form field `LastReadMessageIndex`
- **Returns (parsed)**: `ConversationsV1ServiceServiceUserServiceUserConversation`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceUserServiceUserConversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceUserConversationEnumNotificationLevelOrStr` | `twilio/models/enums/service_user_conversation_enum_notification_level.py` |
| `ConversationsV1ServiceServiceUserServiceUserConversation` | `twilio/models/conversations_v1_service_service_user_service_user_conversation.py` |

### client.conversations_v1_user_conversation.update_user_conversation

- **Route**: `POST /v1/Users/{UserSid}/Conversations/{ConversationSid}`
- **Server**: `default7`
- **Signature**: `def update_user_conversation(user_sid: str, conversation_sid: str, *, notification_level: UserConversationEnumNotificationLevelOrStr | None = None, last_read_timestamp: RFC3339DateTime | None = None, last_read_message_index: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_sid`, `conversation_sid`
- **Params**: `user_sid` — path `UserSid` · `conversation_sid` — path `ConversationSid` · `notification_level` — form field `NotificationLevel` · `last_read_timestamp` — form field `LastReadTimestamp` · `last_read_message_index` — form field `LastReadMessageIndex`
- **Returns (parsed)**: `ConversationsV1UserUserConversation`
- **Returns (raw)**: `ApiResult[ConversationsV1UserUserConversation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserConversationEnumNotificationLevelOrStr` | `twilio/models/enums/user_conversation_enum_notification_level.py` |
| `ConversationsV1UserUserConversation` | `twilio/models/conversations_v1_user_user_conversation.py` |

