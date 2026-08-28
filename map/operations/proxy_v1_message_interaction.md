<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProxyV1MessageInteraction — operations

Accessor: `client.proxy_v1_message_interaction` · Source: `twilio/apis/proxy_v1_message_interaction.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.proxy_v1_message_interaction.create_message_interaction

- **Route**: `POST /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions`
- **Server**: `default10`
- **Signature**: `def create_message_interaction(service_sid: str, session_sid: str, participant_sid: str, *, body: str | None = None, media_url: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `participant_sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `participant_sid` — path `ParticipantSid` · `body` — form field `Body` · `media_url` — form field `MediaUrl`
- **Returns (parsed)**: `ProxyV1ServiceSessionParticipantMessageInteraction`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSessionParticipantMessageInteraction, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServiceSessionParticipantMessageInteraction` | `twilio/models/proxy_v1_service_session_participant_message_interaction.py` |

### client.proxy_v1_message_interaction.fetch_message_interaction

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions/{Sid}`
- **Server**: `default10`
- **Signature**: `def fetch_message_interaction(service_sid: str, session_sid: str, participant_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `participant_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `participant_sid` — path `ParticipantSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ProxyV1ServiceSessionParticipantMessageInteraction`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSessionParticipantMessageInteraction, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServiceSessionParticipantMessageInteraction` | `twilio/models/proxy_v1_service_session_participant_message_interaction.py` |

### client.proxy_v1_message_interaction.list_message_interaction

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions`
- **Server**: `default10`
- **Signature**: `def list_message_interaction(service_sid: str, session_sid: str, participant_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `participant_sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `participant_sid` — path `ParticipantSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListMessageInteractionResponse`
- **Returns (raw)**: `ApiResult[ListMessageInteractionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListMessageInteractionResponse` | `twilio/models/list_message_interaction_response.py` |

