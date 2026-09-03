<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1ParticipantConversationApi — operations

Accessor: `client.conversations_v1_participant_conversation_api` · Source: `twilio_sdk/apis/conversations_v1_participant_conversation_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_participant_conversation_api.list_participant_conversation

- **Route**: `GET /v1/ParticipantConversations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_participant_conversation(*, identity: str | None = None, address: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `identity` — query `Identity` · `address` — query `Address` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListParticipantConversationResponse`
- **Returns (raw)**: `ApiResult[ListParticipantConversationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListParticipantConversationResponse` | `twilio_sdk/models/list_participant_conversation_response.py` |

### client.conversations_v1_participant_conversation_api.list_service_participant_conversation

- **Route**: `GET /v1/Services/{ChatServiceSid}/ParticipantConversations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_service_participant_conversation(chat_service_sid: str, *, identity: str | None = None, address: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `identity` — query `Identity` · `address` — query `Address` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceParticipantConversationResponse`
- **Returns (raw)**: `ApiResult[ListServiceParticipantConversationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceParticipantConversationResponse` | `twilio_sdk/models/list_service_participant_conversation_response.py` |

