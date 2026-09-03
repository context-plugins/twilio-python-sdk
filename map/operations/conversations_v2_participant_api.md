<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV2ParticipantApi — operations

Accessor: `client.conversations_v2_participant_api` · Source: `twilio_sdk/apis/conversations_v2_participant_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v2_participant_api.create_participant_in_conversation

- **Route**: `POST /v2/Conversations/{ConversationSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_participant_in_conversation(conversation_sid: str, *, body: V2ConversationsParticipantsRequest | V2ConversationsParticipantsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2Participant`
- **Returns (raw)**: `ApiResult[ConversationsV2Participant, CreateParticipantInConversationErrorBody]`
- **Error**: `CreateParticipantInConversationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 409, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsParticipantsRequest` | `twilio_sdk/models/v2_conversations_participants_request.py` |
| `V2ConversationsParticipantsRequestDict` | `twilio_sdk/models/v2_conversations_participants_request.py` |
| `ConversationsV2Participant` | `twilio_sdk/models/conversations_v2_participant.py` |
| `CreateParticipantInConversationErrorBody` | `twilio_sdk/errors/create_participant_in_conversation_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_participant_api.fetch_participant2

- **Route**: `GET /v2/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_participant2(conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV2Participant`
- **Returns (raw)**: `ApiResult[ConversationsV2Participant, FetchParticipant2ErrorBody]`
- **Error**: `FetchParticipant2ErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2Participant` | `twilio_sdk/models/conversations_v2_participant.py` |
| `FetchParticipant2ErrorBody` | `twilio_sdk/errors/fetch_participant2_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_participant_api.list_participant_by_conversation

- **Route**: `GET /v2/Conversations/{ConversationSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_participant_by_conversation(conversation_sid: str, *, page_size: int | None = 50, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `page_size` — query `pageSize` · `page_token` — query `pageToken`
- **Returns (parsed)**: `V2ConversationsParticipantsResponse`
- **Returns (raw)**: `ApiResult[V2ConversationsParticipantsResponse, ListParticipantByConversationErrorBody]`
- **Error**: `ListParticipantByConversationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsParticipantsResponse` | `twilio_sdk/models/v2_conversations_participants_response.py` |
| `ListParticipantByConversationErrorBody` | `twilio_sdk/errors/list_participant_by_conversation_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_participant_api.update_participant_in_conversation

- **Route**: `PUT /v2/Conversations/{ConversationSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_participant_in_conversation(conversation_sid: str, sid: str, *, body: V2ConversationsParticipantsRequest1 | V2ConversationsParticipantsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2Participant`
- **Returns (raw)**: `ApiResult[ConversationsV2Participant, UpdateParticipantInConversationErrorBody]`
- **Error**: `UpdateParticipantInConversationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ConversationsParticipantsRequest1` | `twilio_sdk/models/v2_conversations_participants_request1.py` |
| `V2ConversationsParticipantsRequest1Dict` | `twilio_sdk/models/v2_conversations_participants_request1.py` |
| `ConversationsV2Participant` | `twilio_sdk/models/conversations_v2_participant.py` |
| `UpdateParticipantInConversationErrorBody` | `twilio_sdk/errors/update_participant_in_conversation_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

