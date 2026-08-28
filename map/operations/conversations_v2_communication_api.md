<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV2CommunicationApi — operations

Accessor: `client.conversations_v2_communication_api` · Source: `twilio/apis/conversations_v2_communication_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v2_communication_api.create_communication_in_conversation

- **Route**: `POST /v2/Conversations/{ConversationSid}/Communications`
- **Server**: `default7`
- **Signature**: `def create_communication_in_conversation(conversation_sid: str, *, body: V2ConversationsCommunicationsRequest | V2ConversationsCommunicationsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2Communication`
- **Returns (raw)**: `ApiResult[ConversationsV2Communication, CreateCommunicationInConversationErrorBody]`
- **Error**: `CreateCommunicationInConversationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsCommunicationsRequest` | `twilio/models/v2_conversations_communications_request.py` |
| `V2ConversationsCommunicationsRequestDict` | `twilio/models/v2_conversations_communications_request.py` |
| `ConversationsV2Communication` | `twilio/models/conversations_v2_communication.py` |
| `CreateCommunicationInConversationErrorBody` | `twilio/errors/create_communication_in_conversation_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_communication_api.fetch_communication

- **Route**: `GET /v2/Conversations/{ConversationSid}/Communications/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_communication(conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV2Communication`
- **Returns (raw)**: `ApiResult[ConversationsV2Communication, FetchCommunicationErrorBody]`
- **Error**: `FetchCommunicationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2Communication` | `twilio/models/conversations_v2_communication.py` |
| `FetchCommunicationErrorBody` | `twilio/errors/fetch_communication_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_communication_api.list_communication_by_conversation

- **Route**: `GET /v2/Conversations/{ConversationSid}/Communications`
- **Server**: `default7`
- **Signature**: `def list_communication_by_conversation(conversation_sid: str, *, channel_id: str | None = None, page_size: int | None = 50, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `channel_id` — query `channelId` · `page_size` — query `pageSize` · `page_token` — query `pageToken`
- **Returns (parsed)**: `V2ConversationsCommunicationsResponse`
- **Returns (raw)**: `ApiResult[V2ConversationsCommunicationsResponse, ListCommunicationByConversationErrorBody]`
- **Error**: `ListCommunicationByConversationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsCommunicationsResponse` | `twilio/models/v2_conversations_communications_response.py` |
| `ListCommunicationByConversationErrorBody` | `twilio/errors/list_communication_by_conversation_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio/models/accounts_calls_recordings_sid_json201041408_error1.py` |

