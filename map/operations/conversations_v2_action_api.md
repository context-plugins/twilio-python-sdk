<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV2ActionApi — operations

Accessor: `client.conversations_v2_action_api` · Source: `twilio_sdk/apis/conversations_v2_action_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v2_action_api.create_conversation_action

- **Route**: `POST /v2/Conversations/{ConversationId}/Actions`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_conversation_action(conversation_id: str, body: ConversationsV2SendMessageActionRequest | ConversationsV2SendMessageActionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_id`, `body`
- **Params**: `conversation_id` — path `ConversationId` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2Action`
- **Returns (raw)**: `ApiResult[ConversationsV2Action, CreateConversationActionErrorBody]`
- **Error**: `CreateConversationActionErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2SendMessageActionRequest` | `twilio_sdk/models/conversations_v2_send_message_action_request.py` |
| `ConversationsV2SendMessageActionRequestDict` | `twilio_sdk/models/conversations_v2_send_message_action_request.py` |
| `ConversationsV2Action` | `twilio_sdk/models/conversations_v2_action.py` |
| `CreateConversationActionErrorBody` | `twilio_sdk/errors/create_conversation_action_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_action_api.fetch_conversation_action

- **Route**: `GET /v2/Conversations/{ConversationId}/Actions/{ActionId}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_conversation_action(conversation_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_id`, `action_id`
- **Params**: `conversation_id` — path `ConversationId` · `action_id` — path `ActionId`
- **Returns (parsed)**: `ConversationsV2Action`
- **Returns (raw)**: `ApiResult[ConversationsV2Action, FetchConversationActionErrorBody]`
- **Error**: `FetchConversationActionErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2Action` | `twilio_sdk/models/conversations_v2_action.py` |
| `FetchConversationActionErrorBody` | `twilio_sdk/errors/fetch_conversation_action_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

