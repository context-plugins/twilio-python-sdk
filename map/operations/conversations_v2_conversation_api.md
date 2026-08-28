<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV2ConversationApi — operations

Accessor: `client.conversations_v2_conversation_api` · Source: `twilio_sdk/apis/conversations_v2_conversation_api.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v2_conversation_api.create_conversation_with_config

- **Route**: `POST /v2/Conversations`
- **Server**: `default7`
- **Signature**: `def create_conversation_with_config(*, body: V2ConversationsRequest | V2ConversationsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ConversationsV2Conversation`
- **Returns (raw)**: `ApiResult[ConversationsV2Conversation, CreateConversationWithConfigErrorBody]`
- **Error**: `CreateConversationWithConfigErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 409, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsRequest` | `twilio_sdk/models/v2_conversations_request.py` |
| `V2ConversationsRequestDict` | `twilio_sdk/models/v2_conversations_request.py` |
| `ConversationsV2Conversation` | `twilio_sdk/models/conversations_v2_conversation.py` |
| `CreateConversationWithConfigErrorBody` | `twilio_sdk/errors/create_conversation_with_config_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_conversation_api.delete_conversation_async

- **Route**: `DELETE /v2/Conversations/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_conversation_async(sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `idempotency_key` — header `Idempotency-Key`
- **Returns (parsed)**: `ConversationsV2OperationAccepted`
- **Returns (raw)**: `ApiResult[ConversationsV2OperationAccepted, DeleteConversationAsyncErrorBody]`
- **Error**: `DeleteConversationAsyncErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 409, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2OperationAccepted` | `twilio_sdk/models/conversations_v2_operation_accepted.py` |
| `DeleteConversationAsyncErrorBody` | `twilio_sdk/errors/delete_conversation_async_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_conversation_api.fetch_conversation2

- **Route**: `GET /v2/Conversations/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_conversation2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV2Conversation`
- **Returns (raw)**: `ApiResult[ConversationsV2Conversation, FetchConversation2ErrorBody]`
- **Error**: `FetchConversation2ErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2Conversation` | `twilio_sdk/models/conversations_v2_conversation.py` |
| `FetchConversation2ErrorBody` | `twilio_sdk/errors/fetch_conversation2_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_conversation_api.list_conversation_by_account

- **Route**: `GET /v2/Conversations`
- **Server**: `default7`
- **Signature**: `def list_conversation_by_account(*, status: list[Status31OrStr] | None = None, channel_id: str | None = None, page_size: int | None = 50, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query · `channel_id` — query `channelId` · `page_size` — query `pageSize` · `page_token` — query `pageToken`
- **Returns (parsed)**: `V2ConversationsResponse`
- **Returns (raw)**: `ApiResult[V2ConversationsResponse, ListConversationByAccountErrorBody]`
- **Error**: `ListConversationByAccountErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Status31OrStr` | `twilio_sdk/models/enums/status31.py` |
| `V2ConversationsResponse` | `twilio_sdk/models/v2_conversations_response.py` |
| `ListConversationByAccountErrorBody` | `twilio_sdk/errors/list_conversation_by_account_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_conversation_api.patch_conversation_by_id

- **Route**: `PATCH /v2/Conversations/{Sid}`
- **Server**: `default7`
- **Signature**: `def patch_conversation_by_id(sid: str, *, body: V2ConversationsRequest2 | V2ConversationsRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2Conversation`
- **Returns (raw)**: `ApiResult[ConversationsV2Conversation, PatchConversationByIdErrorBody]`
- **Error**: `PatchConversationByIdErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsRequest2` | `twilio_sdk/models/v2_conversations_request2.py` |
| `V2ConversationsRequest2Dict` | `twilio_sdk/models/v2_conversations_request2.py` |
| `ConversationsV2Conversation` | `twilio_sdk/models/conversations_v2_conversation.py` |
| `PatchConversationByIdErrorBody` | `twilio_sdk/errors/patch_conversation_by_id_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_conversation_api.update_conversation_by_id

- **Route**: `PUT /v2/Conversations/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_conversation_by_id(sid: str, *, body: V2ConversationsRequest1 | V2ConversationsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2Conversation`
- **Returns (raw)**: `ApiResult[ConversationsV2Conversation, UpdateConversationByIdErrorBody]`
- **Error**: `UpdateConversationByIdErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsRequest1` | `twilio_sdk/models/v2_conversations_request1.py` |
| `V2ConversationsRequest1Dict` | `twilio_sdk/models/v2_conversations_request1.py` |
| `ConversationsV2Conversation` | `twilio_sdk/models/conversations_v2_conversation.py` |
| `UpdateConversationByIdErrorBody` | `twilio_sdk/errors/update_conversation_by_id_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

