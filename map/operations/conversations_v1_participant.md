<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1Participant — operations

Accessor: `client.conversations_v1_participant` · Source: `twilio_sdk/apis/conversations_v1_participant.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_participant.create_conversation_participant

- **Route**: `POST /v1/Conversations/{ConversationSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_conversation_participant(conversation_sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, identity: str | None = None, messaging_binding_address: str | None = None, messaging_binding_proxy_address: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, messaging_binding_projected_address: str | None = None, role_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `identity` — form field `Identity` · `messaging_binding_address` — form field `MessagingBinding.Address` · `messaging_binding_proxy_address` — form field `MessagingBinding.ProxyAddress` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `messaging_binding_projected_address` — form field `MessagingBinding.ProjectedAddress` · `role_sid` — form field `RoleSid`
- **Returns (parsed)**: `ConversationsV1ConversationConversationParticipant`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ConversationsV1ConversationConversationParticipant` | `twilio_sdk/models/conversations_v1_conversation_conversation_participant.py` |

### client.conversations_v1_participant.create_service_conversation_participant

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_service_conversation_participant(chat_service_sid: str, conversation_sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, identity: str | None = None, messaging_binding_address: str | None = None, messaging_binding_proxy_address: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, messaging_binding_projected_address: str | None = None, role_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `identity` — form field `Identity` · `messaging_binding_address` — form field `MessagingBinding.Address` · `messaging_binding_proxy_address` — form field `MessagingBinding.ProxyAddress` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `messaging_binding_projected_address` — form field `MessagingBinding.ProjectedAddress` · `role_sid` — form field `RoleSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationParticipant`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ConversationsV1ServiceServiceConversationServiceConversationParticipant` | `twilio_sdk/models/conversations_v1_service_service_conversation_service_conversation_participant.py` |

### client.conversations_v1_participant.delete_conversation_participant

- **Route**: `DELETE /v1/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def delete_conversation_participant(conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |

### client.conversations_v1_participant.delete_service_conversation_participant

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def delete_service_conversation_participant(chat_service_sid: str, conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |

### client.conversations_v1_participant.fetch_conversation_participant

- **Route**: `GET /v1/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_conversation_participant(conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ConversationConversationParticipant`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ConversationConversationParticipant` | `twilio_sdk/models/conversations_v1_conversation_conversation_participant.py` |

### client.conversations_v1_participant.fetch_service_conversation_participant

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_service_conversation_participant(chat_service_sid: str, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationParticipant`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConversationServiceConversationParticipant` | `twilio_sdk/models/conversations_v1_service_service_conversation_service_conversation_participant.py` |

### client.conversations_v1_participant.list_conversation_participant

- **Route**: `GET /v1/Conversations/{ConversationSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_conversation_participant(conversation_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConversationParticipantResponse`
- **Returns (raw)**: `ApiResult[ListConversationParticipantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConversationParticipantResponse` | `twilio_sdk/models/list_conversation_participant_response.py` |

### client.conversations_v1_participant.list_service_conversation_participant

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_service_conversation_participant(chat_service_sid: str, conversation_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceConversationParticipantResponse`
- **Returns (raw)**: `ApiResult[ListServiceConversationParticipantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceConversationParticipantResponse` | `twilio_sdk/models/list_service_conversation_participant_response.py` |

### client.conversations_v1_participant.update_conversation_participant

- **Route**: `POST /v1/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_conversation_participant(conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, attributes: str | None = None, role_sid: str | None = None, messaging_binding_proxy_address: str | None = None, messaging_binding_projected_address: str | None = None, identity: str | None = None, last_read_message_index: int | None = None, last_read_timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `attributes` — form field `Attributes` · `role_sid` — form field `RoleSid` · `messaging_binding_proxy_address` — form field `MessagingBinding.ProxyAddress` · `messaging_binding_projected_address` — form field `MessagingBinding.ProjectedAddress` · `identity` — form field `Identity` · `last_read_message_index` — form field `LastReadMessageIndex` · `last_read_timestamp` — form field `LastReadTimestamp`
- **Returns (parsed)**: `ConversationsV1ConversationConversationParticipant`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ConversationsV1ConversationConversationParticipant` | `twilio_sdk/models/conversations_v1_conversation_conversation_participant.py` |

### client.conversations_v1_participant.update_service_conversation_participant

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_service_conversation_participant(chat_service_sid: str, conversation_sid: str, sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, identity: str | None = None, attributes: str | None = None, role_sid: str | None = None, messaging_binding_proxy_address: str | None = None, messaging_binding_projected_address: str | None = None, last_read_message_index: int | None = None, last_read_timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `identity` — form field `Identity` · `attributes` — form field `Attributes` · `role_sid` — form field `RoleSid` · `messaging_binding_proxy_address` — form field `MessagingBinding.ProxyAddress` · `messaging_binding_projected_address` — form field `MessagingBinding.ProjectedAddress` · `last_read_message_index` — form field `LastReadMessageIndex` · `last_read_timestamp` — form field `LastReadTimestamp`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationParticipant`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ConversationsV1ServiceServiceConversationServiceConversationParticipant` | `twilio_sdk/models/conversations_v1_service_service_conversation_service_conversation_participant.py` |

